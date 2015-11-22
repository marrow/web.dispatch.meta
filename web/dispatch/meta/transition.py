# encoding: utf-8

from __future__ import unicode_literals

from inspect import isclass
from collections import deque
from marrow.package.cache import PluginCache

from .util import nodefault, str, range

if __debug__:
	import warnings
	from collections import deque


log = __import__('logging').getLogger(__name__)

unset = object()  # Sentinel value.


class TransitionDispatch(object):
	__slots__ = ['default', 'cache']
	
	def __init__(self, default=None):
		self.cache = PluginCache('web.dispatch')
		
		if not callable(default):
			name = default
			default = self.cache[default]
			
			if isclass(default):
				default = self.cache[name] = default()
		
		elif isclass(default):
			default = default()
		
		self.default = default
		
		if __debug__:
			log.debug("Transition dispatcher prepared.", extra=dict(dispatcher=repr(self)))
		
		super(TransitionDispatch, self).__init__()
	
	def __repr__(self):
		return "TransitionDispatch(0x{id}, default={self.default!r})".format(id=id(self), self=self)
	
	def __call__(self, context, obj, path):
		cache = self.cache  # Local scope access optimiation.
		ppath = deque(path)  # We have a copy of this so we can re-dispatch on it.
		previous = None
		dispatcher = getattr(obj, '__dispatch__', self.default)
		handler = unset
		is_endpoint = False
		
		while not is_endpoint:
			if dispatcher is None:
				raise LookupError("Unable to proceed without a declared (__dispatch__) or default dispatcher.")
			
			if not callable(dispatcher):  # It's probably an entry point reference.
				name = dispatcher
				dispatcher = cache[dispatcher]
				
				if isclass(dispatcher):  # We'll instantiate for you, no configuration, and update the cache.
					dispatcher = cache[name] = dispatcher()
			
			elif isclass(dispatcher):  # We'll instantiate for you, but no configuration this way.
				dispatcher = dispatcher()
			
			#if dispatcher.__class__ == previous.__class__:
			#	break  # We'll cowardly refuse to descend into the same dispatcher infinitely.
			
			if __debug__:
				log.debug("Dispatch transitioning to " + dispatcher.__class__.__name__ + ".", extra=dict(
						dispatcher = repr(dispatcher),
						context = repr(context),
						obj = repr(obj),
						path = list(path)
					))
			
			for event in dispatcher(context, handler, deque(ppath)):
				yield event  # Pass the event up the chain.
				
				consumed, handler, is_endpoint = event[:3]
				
				if consumed:  # Update our copy of the path so we can continue from where we left off.
					if isinstance(consumed, str):
						ppath.popleft()
					else:
						for i in range(len(consumed)):
							ppath.popleft()
				
				if is_endpoint: break  # Skip the rolling-off code.
			
			else:  # Rolling off the loop without hitting is_endpoint means we can transition.
				if handler is unset:  # We didn't actually iterate anything.
					break
				previous = dispatcher
				dispatcher = getattr(obj, '__dispatch__', dispatcher)

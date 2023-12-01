# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0718


"thread"


import queue
import threading
import time
import types
import _thread


from .errors import Errors


def __dir__():
    return (
        'Thread',
        'launch',
        'lock',
        'name'
    )


__all__ = __dir__()


lock = _thread.allocate_lock()


class Thread(threading.Thread):

    debug     = False

    def __init__(self, func, thrname, *args, daemon=True, **kwargs):
        ""
        super().__init__(None, self.run, thrname, (), {}, daemon=daemon)
        self._result   = None
        self.name      = thrname or name(func)
        self.queue     = queue.Queue()
        self.sleep     = None
        self.starttime = time.time()
        self.queue.put_nowait((func, args))

    def __iter__(self):
        ""
        return self

    def __next__(self):
        ""
        for k in dir(self):
            yield k

    def join(self, timeout=None) -> type:
        ""
        super().join(timeout)
        return self._result

    def run(self) -> None:
        ""
        func, args = self.queue.get()
        try:
            self._result = func(*args)
        except Exception as exc:
            if Thread.debug:
                raise
            Errors.add(exc)
            if args:
                args[0].ready()


def launch(func, *args, **kwargs) -> Thread:
    nme = kwargs.get("name", name(func))
    thread = Thread(func, nme, *args, **kwargs)
    thread.start()
    return thread


def name(obj) -> str:
    typ = type(obj)
    if isinstance(typ, types.ModuleType):
        return obj.__name__
    if '__self__' in dir(obj):
        return f'{obj.__self__.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj) and '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    if '__class__' in dir(obj):
        return f"{obj.__class__.__module__}.{obj.__class__.__name__}"
    if '__name__' in dir(obj):
        return f'{obj.__class__.__name__}.{obj.__name__}'
    return None

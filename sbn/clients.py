# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,W0212,E0402,W0201,W0613,E1120,R0902,W0105,W0612
# pylint: disable=W0718


"clientele"


import inspect
import os
import time
import threading


from .brokers import Broker
from .default import Default
from .methods import parse
from .objects import Object
from .reactor import Reactor


def __dir__():
    return (
            'Client',
            'Event',
            'mods',
           )


__all__ = __dir__()


class Event(Default):

    def __init__(self):
        Object.__init__(self)
        self._ready = threading.Event()
        self._thr = None
        self.result = []
        self.type = "command"

    def ready(self) -> None:
        self._ready.set()

    def reply(self, txt) -> None:
        self.result.append(txt)

    def show(self):
        Broker.show(self)

    def wait(self) -> []:
        if self._thr:
            self._thr.join()
        self._ready.wait()
        return self.result


class Client(Reactor):

    cmds = {}
    skip = ["PING", "PONG", 'PRIVMSG']

    def __init__(self):
        Reactor.__init__(self)
        Broker.add(self)
        self.register("command", command)

    @staticmethod
    def add(func):
        Client.cmds[func.__name__] = func

    def announce(self, txt):
        self.raw(txt)

    @staticmethod
    def debug(txt):
        donext = False
        for skp in Client.skip:
            if skp in txt:
                donext = True
        if donext:
            return
        Client.output(txt)

    def event(self, txt):
        evt = Event()
        evt.txt = txt
        evt.orig = object.__repr__(self)
        evt.type = "event"
        return evt

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)

    @staticmethod
    def scan(mod) -> None:
        for key, cmd in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Client.add(cmd)

    def wait(self):
        while not self._stopped.is_set():
            time.sleep(1.0)


"utility"


def mods(path):
    res = []
    for fnm in os.listdir(path):
        if fnm.endswith("~"):
            continue
        if not fnm.endswith(".py"):
            continue
        if fnm in ["__main__.py", "__init__.py"]:
            continue
        res.append(fnm[:-3])
    return sorted(res)


"methods"


def command(obj):
    parse(obj, obj.txt)
    obj.type = "command"
    func = Client.cmds.get(obj.cmd, None)
    if func:
        try:
            func(obj)
            Broker.show(obj)
        except Exception as ex:
            exc = ex.with_traceback(ex.__traceback__)
            Client.errors.append(exc)
    obj.ready()

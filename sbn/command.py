# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402
# flake8: noqa


"commands"


import inspect


from .listens import Bus
from .errored import Errors
from .utility import mods, parse


class Commands:

    cmds = {}
    errors = []

    @staticmethod
    def add(func):
        Commands.cmds[func.__name__] = func

    @staticmethod
    def handle(evt):
        if "txt" in dir(evt):
            parse(evt, evt.txt)
            func = Commands.cmds.get(evt.cmd, None)
            if func:
                try:
                    func(evt)
                    Bus.show(evt)
                except Exception as ex:
                    exc = ex.with_traceback(ex.__traceback__)
                    Errors.errors.append(exc)
        evt.ready()

    @staticmethod
    def remove(name):
        try:
            del Commands.cmds[name]
        except KeyError:
            pass

    @staticmethod
    def scan(mod) -> None:
        for key, cmd in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Commands.add(cmd)


def scan(pkg, modstr, init=None, doall=False) -> None:
    path = pkg.__path__[0]
    threads = []
    for modname in mods(path):
        if not doall and modname not in modstr:
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        Commands.scan(module)
        if init and "init" in dir(module):
            threads.append(launch(module.start, name=modname))
    return threads

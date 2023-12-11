# This file is placed in the Public Domain.
#
#


import inspect


from .command import Commands
from .errors  import Errors
from .event   import Event
from .object  import Object
from .storage import Storage
from .utility import spl


def __dir__():
    return (
        'command',
        'debug',
        'scan'
    )


def command(txt):
    evn = Event()
    evn.txt = txt
    Commands.handle(evn)
    evn.wait()
    return evn


def debug(txt):
    if Errors.output and not Errors.skip(txt):
        Errors.output(txt)


def scan(pkg, modstr, initer=False) -> []:
    threads = []
    for modname in spl(modstr):
        module = getattr(pkg, modname, None)
        if not module:
            continue
        for key, cmd in inspect.getmembers(module, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmd.__code__.co_varnames:
                Commands.add(cmd)
        for key, clz in inspect.getmembers(module, inspect.isclass):
            if key.startswith("cb"):
                continue
            if not issubclass(clz, Object):
                continue
            Storage.add(clz)
        if initer and "init" in dir(module):
            threads.append(launch(module.init, name=f"init {modname}"))
    return threads

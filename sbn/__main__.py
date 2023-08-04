# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402
# flake8: noqa


"runtime"


import os
import sys


from .command import Commands, scan
from .console import CLI, Console
from .errored import Errors
from .message import Event
from .objects import Persist
from .runtime import Cfg, init
from .threads import launch
from .utility import banner, daemon, parse, wait, wrap


from . import modules


Cfg.mod = "bsc"
Persist.workdir = os.path.expanduser(f"~/.{Cfg.name}")



def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    if "v" in Cfg.opts:
        Errors.raw = print
        Errors.verbose = True
    if "d" in Cfg.opts:
        daemon()
        scan(modules, Cfg.mod)
        wait()
    elif "c" in Cfg.opts:
        print(banner(Cfg))
        csl = Console()
        scan(modules, Cfg.mod)
        csl.start()
        wait(Errors.wait)
    else:
        cli = CLI()
        scan(modules, Cfg.mod, False, True)
        evt = Event()
        evt.orig = repr(cli)
        evt.txt = Cfg.otxt
        evt._thr = launch(Commands.handle, evt)
        evt.wait()


def wrapped():
    wrap(main)


if __name__ == "__main__":
    wrapped()

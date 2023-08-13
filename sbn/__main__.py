# This file is placed in the Public Domain.
#
# pylint: disable=C0116,W0212,W0611,E0402,E0611
# flake8: noqa=F401


"main"


import os
import readline
import sys
import termios


from .command import Commands
from .console import CLI, Console
from .errored import Errors
from .listens import Bus
from .message import Event
from .objfunc import parse
from .runtime import Cfg, scan
from .storage import Storage
from .threads import launch
from .utility import banner, wait


from . import modules


def __dir__():
    return (
            'Cfg',
           )


Cfg.mod = "bsc,err,mdl,req,sts,thr"


Storage.workdir = os.path.expanduser(f"~/.{Cfg.name}")


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    with open('/dev/null', 'r', encoding="utf-8") as sis:
        os.dup2(sis.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as sos:
        os.dup2(sos.fileno(), sys.stdout.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as ses:
        os.dup2(ses.fileno(), sys.stderr.fileno())


def wrap(func) -> None:
    if "d" in Cfg.opts:
        Errors.debug("terminal disabled")
        return
    old = termios.tcgetattr(sys.stdin.fileno())
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
    Errors.wait()


def main():
    if "v" in Cfg.opts:
        Errors.raw = print
        Errors.verbose = True
        print(banner(Cfg))
    if "d" in Cfg.opts:
        daemon()
        scan(modules, Cfg.mod, True)
        wait()
    elif "c" in Cfg.opts:
        csl = Console()
        scan(modules, Cfg.mod, True)
        Bus.wait()
        launch(csl.loop)
        wait(Errors.wait)
    else:
        cli = CLI()
        print(Cfg.mod)
        scan(modules, Cfg.mod, False, True)
        evt = Event()
        evt.orig = object.__repr__(cli)
        evt.txt = Cfg.otxt
        Commands.handle(evt)
        evt.wait()


def wrapped():
    parse(Cfg, " ".join(sys.argv[1:]))
    if "d" in Cfg.opts:
        main()
    else:
        wrap(main)


if __name__ == "__main__":
    wrapped()

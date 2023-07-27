# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212


"runtime"


import os
import readline
import sys
import termios
import time
import _thread


sys.path.insert(0, os.getcwd())


from . import Bus, Cfg, Command, Event, Log, Object, Reactor
from . import launch, parse, scan, update, wait, waiter


from . import modules


Cfg.mod = "bsc"
#Cfg.name = sys.argv[0].split(os.sep)[-1]
Cfg.name = __file__.split(os.sep)[-2]
Cfg.verbose = False
Cfg.version = 250
Cfg.workdir = os.path.expanduser(f"~/.{Cfg.name}")


class CLI(Reactor):

    def __init__(self):
        Reactor.__init__(self)
        Bus.add(self)
        self.register("event", Command.handle)

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)


class Console(CLI):

    def __init__(self):
        CLI.__init__(self)

    def handle(self, evt):
        Command.handle(evt)
        evt.wait()

    def poll(self):
        try:
            return self.event(input("> "))
        except EOFError:
            _thread.interrupt_main()


def banner(names, version):
    times = time.ctime(time.time())
    return f"{names.upper()} {version} {times}"


def cprint(txt):
    print(txt)
    sys.stdout.flush()


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    sis = open('/dev/null', 'r', encoding="utf-8")
    os.dup2(sis.fileno(), sys.stdin.fileno())
    sos = open('/dev/null', 'a+', encoding="utf-8")
    ses = open('/dev/null', 'a+', encoding="utf-8")
    os.dup2(sos.fileno(), sys.stdout.fileno())
    os.dup2(ses.fileno(), sys.stderr.fileno())


def wrap(func) -> None:
    old = termios.tcgetattr(sys.stdin.fileno())
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
        waiter()


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    if "v" in Cfg.opts:
        Log.raw = cprint
    if "d" in Cfg.opts:
        daemon()
        scan(modules, Cfg.mod, True, "a" in Cfg.opts)
        wait()
    elif "c" in Cfg.opts:
        print(banner(Cfg.name, Cfg.version))
        csl = Console()
        scan(modules, Cfg.mod, True, "a" in Cfg.opts)
        launch(csl.loop)
        wait(waiter)
    else:
        cli = CLI()
        scan(modules, Cfg.mod, False, True)
        evt = Event()
        evt.orig = repr(cli)
        evt.txt = Cfg.otxt
        Command.handle(evt)


if __name__ == "__main__":
    wrap(main)

# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402
# flake8: noqa


"console"


import sys
import threading
import _thread


from .command import Commands
from .listens import Bus
from .reactor import Reactor


class CLI(Reactor):

    def __init__(self):
        Reactor.__init__(self)
        Bus.add(self)
        self.register("event", Commands.handle)

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)


class Console(CLI):

    prompting = threading.Event()

    def handle(self, evt):
        Commands.handle(evt)
        evt.wait()

    def prompt(self):
        self.prompting.set()
        x = input("> ")
        self.prompting.clear()
        return x
        
    def poll(self):
        try:
            return self.event(self.prompt())
        except EOFError:
            _thread.interrupt_main()


def cprint(txt):
    if Console.prompting.is_set():
        txt = "\n" + txt
    print(txt)
    Console.prompting.clear()
    sys.stdout.flush()

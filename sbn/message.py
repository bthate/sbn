# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402
# flake8: noqa


"happens"


import threading


from .objects import Default


class Event(Default):

    def __init__(self):
        Default.__init__(self)
        self._ready = threading.Event()
        self._thr = None
        self.result = []

    def ready(self) -> None:
        self._ready.set()

    def reply(self, txt) -> None:
        self.result.append(txt)

    def wait(self) -> []:
        if self._thr:
            self._thr.join()
        self._ready.wait()
        return self.result

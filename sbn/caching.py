# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,R0912,R0915,W0105,E0402,R0903


"output cache"


class Cache:


    def __init__(self):
        self.cache = {}

    def size(self, chan):
        if chan in self.cache:
            return len(self.cache.get(chan, []))
        return 0

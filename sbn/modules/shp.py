# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"shopping list"


import time


from ..objects import Object, Persist
from ..objects import find, fntime, write
from ..utility import laps


class Shop(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''

    def size(self):
        return len(self.__dict__)

    def length(self):
        return len(self.__dict__)


def got(event):
    if not event.args:
        event.reply("got <txt>")
        return
    selector = {'txt': event.args[0]}
    nr = 0
    for obj in find('shop', selector):
        nr += 1
        obj.__deleted__ = True
        write(obj)
        event.reply('ok')
    if not nr:
        event.reply("no shops")


def shp(event):
    if not event.rest:
        nmr = 0
        for obj in find('shop'):
            lap = laps(time.time()-fntime(obj.__oid__))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply("no shops")
        return
    obj = Shop()
    obj.txt = event.rest
    write(obj)
    event.reply('ok')

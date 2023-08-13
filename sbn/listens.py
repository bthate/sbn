# This file is placed in the Public Domain.
#
# pylint: disable=C0115,C0116,E0402


"reactor"


from .errored import Errors
from .utility import name


def __dir__():
    return (
            'Bus',
           )


class Bus:

    objs = []

    @staticmethod
    def add(obj) -> None:
        Errors.debug(f"bus add {name(obj)}")
        Bus.objs.append(obj)

    @staticmethod
    def announce(txt) -> None:
        for obj in Bus.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        for obj in Bus.objs:
            if object.__repr__(obj) == orig:
                return obj
        return None

    @staticmethod
    def bytype(typ):
        for obj in Bus.objs:
            if typ in object.__repr__(obj):
                return obj
        return None

    @staticmethod
    def remove(obj) -> None:
        try:
            Bus.objs.remove(obj)
        except ValueError:
            pass

    @staticmethod
    def say(orig, txt, channel=None) -> None:
        obj = Bus.byorig(orig)
        if obj:
            if channel:
                obj.say(channel, txt)
            else:
                obj.raw(txt)

    @staticmethod
    def show(event) -> None:
        for txt in event.result:
            Bus.say(event.orig, txt, event.channel)

    @staticmethod
    def wait():
        bot = Bus.bytype("IRC")
        if bot:
            Errors.debug(f"waiting on {bot.cfg.server}")
            bot.wait()

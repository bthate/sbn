# This file is placed in the Public Domain.
#
# pylint: disable=C0115,E0402.R0903


"configurations"


from .objects import Object


class Default(Object):

    __default__ = ""

    def __init__(self):
        Object.__init__(self)
        self.__default__ = Default.__default__

    def __getattr__(self, key):
        return self.__dict__.get(key, self.__default__)

# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"runtime"


import os
import sys


from .errored import Errors
from .objects import Default
from .threads import launch
from .utility import spl


Cfg = Default()
Cfg.name = __file__.split(os.sep)[-2]
Cfg.version = "250"


def init(pkg, mods):
    res = []
    for modname in spl(mods):
        mod = getattr(pkg, modname, None)
        if mod and "init" in dir(mod):
            Errors.debug("init %s" % modname)
            res.append(launch(mod.init))
    return res

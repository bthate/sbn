# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W


"debug"


from ..runtime import Cfg


def dbg(event):
    if Cfg.error:
        event.reply("raising")
        raise Exception("debug")
    else:
        event.reply("error is not enabled")

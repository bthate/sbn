# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0401,W0622
# flake8: noqa


"list of bots"


from ..listens import Bus


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(str(Bus.objs[index]))
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(' | '.join([repr(obj).split()[0].split(".")[-1] for obj in Bus.objs]))

# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0401,W0622
# flake8: noqa


"status of bots"


from ..listens import Bus


def sts(event):
    nmr = 0
    for bot in Bus.objs:
        if 'state' in dir(bot):
            event.reply(str(bot.state))
            nmr += 1
    if not nmr:
        event.reply("no status")

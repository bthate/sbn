# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"basic commands"


from ..command import Commands


def cmd(event):
    event.reply(",".join(sorted(Commands.cmds)))

# This file is placed in the Public Domain.
#
# pylint: disable=C0116,E0402


"basic commands"


from ..command import Commands


def __dir__():
    return (
            "cmd",
           )


def cmd(event):
    event.reply(",".join(sorted(Commands.cmds)))

# This file is placed in the Public Domain.
# pylint: disable=E0402

"list of commands"


from ..command import Commands


def cmd(event):
    """ available commands """
    event.reply(",".join(sorted(Commands.cmds.keys())))

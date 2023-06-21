# This file is placed in the Public Domain.
#
#


"reload"


from ..command import Commands


import sbn.modules


def rld(event):
    if not event.args:
         event.reply("rld <modname>")
         return
    modname = event.args[0]
    mod = getattr(sbn.modules, modname)
    if not mod:
        event.reply(f"{modname} is not available")
        return
    Commands.scan(mod)
    event.reply(f"reloaded {modname}")


def unl(event):
    if not event.args:
         event.reply("rld <modname>")
         return
    modname = event.args[0]
    if modname == "rld":
        event.reply("won't unload myself")
        return
    mod = getattr(sbn.modules, modname)
    if not mod:
        event.reply(f"{modname} is not available")
        return
    Commands.remove(mod)
    event.reply(f"unloaded {modname}")

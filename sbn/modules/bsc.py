# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0401,W0622


"basic commands"


import io
import os
import threading
import time
import traceback


from .. import Bus, Command, Error, Object
from .. import laps, printable, update


try:
    import mod as modules
except ModuleNotFoundError:
    modules = None


STARTTIME = time.time()


def __dir__():
    return (
            "cmd",
            "err",
            "flt",
            'mod',
            'sts',
            "thr",
           )


__all__ = __dir__()


def cmd(event):
    event.reply(",".join(sorted(Command.cmds)))


def err(event):
    nmr = 0
    for exc in Error.errors:
        stream = io.StringIO(
                             traceback.print_exception(
                                                       type(exc),
                                                       exc,
                                                       exc.__traceback__
                                                      )
                            )
        for line in stream.readlines():
            event.reply(line)
            nmr += 1
    if not nmr:
        event.reply("no error")


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(printable(Bus.objs[index]))
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(' | '.join([repr(obj).split()[0].split(".")[-1] for obj in Bus.objs]))


def mod(event):
    path = modules.__path__[0]
    modlist = [
               x[:-3] for x in os.listdir(path)
               if x.endswith(".py")
               and x not in ["__main__.py", "__init__.py"]
              ]
    event.reply(",".join(sorted(modlist)))


def sts(event):
    nmr = 0
    for bot in Bus.objs:
        if 'state' in dir(bot):
            event.reply(printable(bot.state, skip='lastline'))
            nmr += 1
    if not nmr:
        event.reply("no status")


def thr(event):
    result = []
    for thread in sorted(threading.enumerate(), key=lambda x: x.name):
        if str(thread).startswith('<_'):
            continue
        obj = Object()
        update(obj, vars(thread))
        if getattr(obj, 'sleep', None):
            uptime = obj.sleep - int(time.time() - obj.state.latest)
        elif getattr(obj, 'starttime', None):
            uptime = int(time.time() - obj.starttime)
        else:
            uptime = int(time.time() - STARTTIME)
        result.append((uptime, thread.name))
    res = []
    for uptime, txt in sorted(result, key=lambda x: x[1]):
        lap = laps(uptime)
        res.append(f'{txt}/{lap}')
    if res:
        event.reply(' '.join(res))
    else:
        event.reply('no threads')

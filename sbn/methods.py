# This file is placed in the Public Domain.
#
# pylint: disable=C0112,C0115,C0116,W0105,R0903,E0402,C0209


"functions"


import datetime
import uuid


from .brokers import Broker
from .finding import fntime
from .objects import fqn, keys, read
from .storage import Storage


def __dir__():
    return (
            'command',
            'fetch',
            'fmt',
            'fqn',
            'ident',
            'last',
            'parse',
            'search',
            'sync'
           )            


def fetch(obj, pth):
    path = Storage.store(pth)
    return read(obj, path)


def fmt(obj, args=[], skip=[]) -> str:
    if not args:
        args = keys(obj)
    txt = ""
    for key in sorted(args):
        if key == "__fnm__":
            continue
        if key in skip:
            continue
        try:
            value = obj[key]
        except KeyError:
            continue
        if isinstance(value, str) and len(value.split()) >= 2:
            txt += f'{key}="{value}" '
        else:
            txt += f'{key}={value} '
    return txt.strip()


def fqn(obj) -> str:
    kin = str(type(obj)).split()[-1][1:-2]
    if kin == "type":
        kin = obj.__name__
    return kin


def ident(obj) -> str:
    return os.path.join(
                        fqn(obj),
                        str(uuid.uuid4().hex),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )


def last(obj, selector=None) -> None:
    if selector is None:
        selector = {}
    result = sorted(
                    find(fqn(obj), selector),
                    key=lambda x: fntime(x.__fnm__)
                   )
    if result:
        inp = result[-1]
        update(obj, inp)
        if "__fnm__" in inp:
            obj.__fnm__ = inp.__fnm__


def parse(obj, txt=None) -> None:
    args = []
    obj.args = []
    obj.cmd = obj.cmd or ""
    obj.gets = obj.gets or {}
    obj.hasmods = False
    obj.mod = obj.mod or ""
    obj.opts = obj.opts or ""
    obj.sets = obj.sets or {}
    obj.otxt = txt or ""
    _nr = -1
    for spli in obj.otxt.split():
        if spli.startswith("-"):
            try:
                obj.index = int(spli[1:])
            except ValueError:
                obj.opts += spli[1:]
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                obj.hasmods = True
                if obj.mod:
                    obj.mod += f",{value}"
                else:
                    obj.mod = value
                continue
            obj.sets[key] = value
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            obj.gets[key] = value
            continue
        _nr += 1
        if _nr == 0:
            obj.cmd = spli
            continue
        args.append(spli)
    if args:
        obj.args = args
        obj.txt = obj.cmd or ""
        obj.rest = " ".join(obj.args)
        obj.txt = obj.cmd + " " + obj.rest
    else:
        obj.txt = obj.cmd


def search(obj, selector) -> bool:
    res = False
    for key, value in items(selector):
        try:
            val = obj[key]
        except KeyError:
            continue
        if str(value) in str(val):
            res = True
            break
    return res


def sync(obj, pth=None):
    if "__fnm__" in obj:
        pth = obj.__fnm__
        del obj.__fnm__
    if not pth:
        pth = ident(obj)
    pth = Storage.store(pth)
    cdir(pth)
    write(obj, pth)
    obj.__fnm__ = pth

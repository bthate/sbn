# This file is placed in the Public Domain.
#
# pylint: disable=C0112,C0115,C0116,W0105,R0903,E0402,C0209


"persistence"


import datetime
import inspect
import os
import pathlib
import sys
import time
import uuid


from .objects import Object, keys, kind, read, search, update, write


def __dir__():
    return (
            'Storage',
            'edit',
            'fetch',
            'find',
            'last',
            'prt',
            'sync'
           )


__all__ = __dir__()


class Storage:

    classes = {}
    workdir = os.path.expanduser('~/.%s' % __file__.split(os.sep)[-2])

    @staticmethod
    def add(clz):
        if not clz:
            return
        name = str(clz).split()[1][1:-2]
        Storage.classes[name] = clz

    @staticmethod
    def long(name):
        split = name.split(".")[-1].lower()
        res = None
        for named in keys(Storage.classes):
            if split in named.split(".")[-1].lower():
                res = named
                break
        return res

    @staticmethod
    def path(pth):
        cdir(pth)
        return os.path.join(Storage.store(), pth)

    @staticmethod
    def scan(mod) -> None:
        for key, clz in inspect.getmembers(mod, inspect.isclass):
            if key.startswith("cb"):
                continue
            if not issubclass(clz, Object):
                continue
            Storage.add(clz)

    @staticmethod
    def store(pth=""):
        return os.path.join(Storage.workdir, "store", pth)


"utility"


def cdir(pth) -> None:
    if not pth.endswith(os.sep):
        pth = os.path.dirname(pth)
    pth = pathlib.Path(pth)
    os.makedirs(pth, exist_ok=True)


def doskip(txt, skipping) -> bool:
    for skp in spl(skipping):
        if skp in txt:
            return True
    return False


def files() -> []:
    return os.listdir(Storage.store())


def find(mtc, selector=None) -> []:
    if selector is None:
        selector = {}
    for fnm in reversed(sorted(fns(mtc), key=fntime)):
        clzname = fnclass(fnm)
        clz = sys.modules.get(clzname, None)
        if not clz:
            clz = Object
        obj = clz()
        fetch(obj, fnm)
        if '__deleted__' in obj:
            continue
        if selector and not search(obj, selector):
            continue
        obj.__fnm__ = fnm
        yield obj


def fns(mtc) -> []:
    dname = ''
    clz = Storage.long(mtc)
    if clz:
        path = Storage.path(clz)
        for rootdir, dirs, _files in os.walk(path, topdown=False):
            if dirs:
                dname = sorted(dirs)[-1]
                if dname.count('-') == 2:
                    ddd = os.path.join(rootdir, dname)
                    fls = sorted(os.listdir(ddd))
                    if fls:
                        yield strip(os.path.join(ddd, fls[-1]))


def fnclass(fnm):
    return fnm.split(os.sep)[-4]


def fntime(daystr) -> float:
    daystr = daystr.replace('_', ':')
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    else:
        timed = 0
    return timed


def fqn(obj) -> str:
    kin = str(type(obj)).split()[-1][1:-2]
    if kin == "type":
        kin = obj.__name__
    return kin


def spl(txt) -> []:
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def strip(path) -> str:
    return os.sep.join(path.split(os.sep)[-4:])


"methods"


def edit(obj, setter, skip=False):
    try:
        setter = vars(setter)
    except (TypeError, ValueError):
        pass
    if not setter:
        setter = {}
    for key, val in setter.items():
        if skip and val == "":
            continue
        try:
            setattr(obj, key, int(val))
            continue
        except ValueError:
            pass
        try:
            setattr(obj, key, float(val))
            continue
        except ValueError:
            pass
        if val in ["True", "true"]:
            setattr(obj, key, True)
        elif val in ["False", "false"]:
            setattr(obj, key, False)
        else:
            setattr(obj, key, val)


def fetch(obj, pth):
    path = Storage.store(pth)
    return read(obj, path)


def ident(obj) -> str:
    return os.path.join(
                        kind(obj),
                        str(uuid.uuid4().hex),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )


def last(obj, selector=None) -> None:
    if selector is None:
        selector = {}
    result = sorted(
                    find(kind(obj), selector),
                    key=lambda x: fntime(x.__fnm__)
                   )
    if result:
        inp = result[-1]
        update(obj, inp)
        if "__fnm__" in inp:
            obj.__fnm__ = inp.__fnm__


def format(obj, args="") -> str:
    if args:
        keyz = args.split(",")
    else:
        keyz = keys(obj)
    txt = ""
    for key in sorted(keyz):
        try:
            value = obj[key]
        except KeyError:
            continue
        if isinstance(value, str) and len(value.split()) >= 2:
            txt += f'{key}="{value}" '
        else:
            txt += f'{key}={value} '
    return txt.strip()


def search(obj, selector) -> bool:
    res = False
    for key, value in items(selector):
        try:
            val = obj[key]
            if str(value) in str(val):
                res = True
                break
        except KeyError:
            continue
    return res


def sync(obj, pth=None):
    if "__fnm__" in obj:
        pth = obj.__fnm__
    if not pth:
        pth = ident(obj)
    pth = Storage.store(pth)
    cdir(pth)
    write(obj, pth)

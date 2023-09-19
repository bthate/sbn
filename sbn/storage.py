# This file is placed in the Public Domain.
#
# pylint: disable=C0112,C0115,C0116,W0105,R0903,E0402,C0209


"persistence"


import datetime
import inspect
import os
import uuid


from .finding import find
from .objects import Object, fqn, keys, read, write
from .utility import cdir, fntime, strip


def __dir__():
    return (
            'Storage',
            'fetch',
            'find',
            'fntime',
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


"methods"


def ident(obj) -> str:
    return os.path.join(
                        fqn(obj),
                        str(uuid.uuid4().hex),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )


def fetch(obj, pth):
    path = Storage.store(pth)
    return read(obj, path)


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

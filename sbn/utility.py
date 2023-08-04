# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402
# flake8: noqa


"utilities"


import os
import sys
import termios
import time
import types


def banner(cfg):
    if cfg.mod:
        mods = cfg.mod.upper()
    else:
        mods = "CONSOLE"
    return f"{cfg.name.upper()} {cfg.version} {mods} {cfg.opts}" 


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    sis = open('/dev/null', 'r', encoding="utf-8")
    os.dup2(sis.fileno(), sys.stdin.fileno())
    sos = open('/dev/null', 'a+', encoding="utf-8")
    ses = open('/dev/null', 'a+', encoding="utf-8")
    os.dup2(sos.fileno(), sys.stdout.fileno())
    os.dup2(ses.fileno(), sys.stderr.fileno())


def laps(seconds, short=True) -> str:
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    year = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    years = int(nsec/year)
    nsec -= years*year
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if years:
        txt += f"{years}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if nrdays and short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def mods(path):
    return [
            x[:-3].strip() for x in os.listdir(path)
            if x.endswith(".py")
            and x not in ["__init__.py", "__main__.py"]
           ]


def name(obj) -> str:
    typ = type(obj)
    if isinstance(typ, types.ModuleType):
        return obj.__name__
    if '__self__' in dir(obj):
        return '%s.%s' % (obj.__self__.__class__.__name__, obj.__name__)
    if '__class__' in dir(obj) and '__name__' in dir(obj):
        return '%s.%s' % (obj.__class__.__name__, obj.__name__)
    if '__class__' in dir(obj):
        return obj.__class__.__name__
    if '__name__' in dir(obj):
        return '%s.%s' % (obj.__class__.__name__, obj.__name__)
    return None


def parse(self, txt=None) -> None:
    args = []
    self.args = []
    self.cmd = self.cmd or ""
    self.gets = self.gets or {}
    self.mod = self.mod or ""
    self.opts = self.opts or ""
    self.sets = self.sets or {}
    self.otxt = txt or ""
    _nr = -1
    for spli in self.otxt.split():
        if spli.startswith("-"):
            try:
                self.index = int(spli[1:])
            except ValueError:
                self.opts += spli[1:]
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                if self.mod:
                    self.mod += f",{value}"
                else:
                    self.mod = value
                continue
            self.sets[key] = value
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            self.gets[key] = value
            continue
        _nr += 1
        if _nr == 0:
            self.cmd = spli
            continue
        args.append(spli)
    if args:
        self.args = args
        self.txt = self.cmd or ""
        self.rest = " ".join(self.args)
        self.txt = self.cmd + " " + self.rest
    else:
        self.txt = self.cmd


def skip(txt, skipping) -> bool:
    for skp in spl(skipping):
        if skp in txt:
            return True
    return False


def spl(txt) -> []:
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def tme():
    return time.ctime(time.time()).split()[3]


def wait(func=None):
    while 1:
        time.sleep(1.0)
        if func:
            func()


def wrap(func) -> None:
    old = termios.tcgetattr(sys.stdin.fileno())
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)

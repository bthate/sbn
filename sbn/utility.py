# This file is placed in the Public Domain.
#
#


"utilities"


import os


def __dir__():
    return (
            'mods',
            'skip',
            'spl'
           ) 


def mods(path):
    res = []
    for fnm in os.listdir(path):
        if fnm.endswith("~"):
            continue
        if not fnm.endswith(".py"):
            continue
        if fnm in ["__main__.py", "__init__.py"]:
            continue
        res.append(fnm[:-3])
    return sorted(res)


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

# This file is placed in the Public Domain.
#
#


"utilities"


def spl(txt) -> []:
    try:
        res = txt.split(',')
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]

# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"errors"


import io
import traceback


from ..error import Error

def __dir__():
    return (
            'err',
           )


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

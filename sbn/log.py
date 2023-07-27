# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R,W0212,W0718,E0402


"logging"


import io
import traceback


from .utils import skip


class Log:

    skip = 'PING,PONG,PRIVMSG'
    verbose = False
    errors = []

    @staticmethod
    def debug(txt) -> None:
        if not skip(txt, Log.skip):
            Log.raw(txt)

    @staticmethod
    def handle(exc):
        excp = exc.with_traceback(exc.__traceback__)
        Log.errors.append(excp)

    @staticmethod
    def raw(txt) -> None:
        pass


def waiter(clear=True):
    got = []
    for ex in Log.errors:
        stream = io.StringIO(
                             traceback.print_exception(
                                                       type(ex),
                                                       ex,
                                                       ex.__traceback__
                                                      )
                            )
        for line in stream.readlines():
            Log.debug(line)
        got.append(ex)
    if clear:
        for exc in got:
            if exc in Log.errors:
                Log.errors.remove(exc)

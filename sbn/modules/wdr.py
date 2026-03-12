# This file is placed in the Public Domain.


"working directory"


from sbn.persist import Workdir


def wdr(event):
    event.reply(Workdir.workdir())

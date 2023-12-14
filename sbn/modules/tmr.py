# This file is placed in the Public Domain.
#
#


"timer"


import time


from sbn import Event, Timer
from sbn.utils import NoDate, day, now, to_time, to_day, get_day, get_hour
from sbn.utils import laps, launch


def tmr(event):
    if not event.rest:
        event.reply("tmr <txt with time>")
        return
    seconds = 0
    line = ""
    for word in event.args:
        if word.startswith("+"):
             try:
                 seconds = int(word[1:])
             except:
                 event.reply("%s is not an integer" % seconds)
                 return
        else:
            line += word + " "
    if seconds:
        target = time.time() + seconds
    else:
        try:
            target = get_day(event.rest)
        except NoDate:
            target = to_day(day())
        hour =  get_hour(event.rest)
        if hour:
            target += hour
    if not target or time.time() > target:
        event.reply("already passed given time.")
        return
    diff = target - time.time()
    event.reply("ok " +  laps(diff))
    event.show()
    event.result = []
    event.result.append(event.rest)
    timer = Timer(diff, event.show)
    launch(timer.start)

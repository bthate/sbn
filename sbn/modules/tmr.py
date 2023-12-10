# This file is placed in the Public Domain.
#
#


"timer"


import time


from sbn.event  import Event
from sbn.timer  import NoDate, Timer, to_time, to_day, get_day, get_hour
from sbn.thread import launch
from sbn.utils  import day, now

def tmr(event):
    if not event.rest:
        event.reply("tmr <txt with time>")
        return
    seconds = 0
    line = ""
    for word in event._parsed.args:
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
            target = get_day(event._parsed.rest)
        except NoDate:
            target = to_day(day())
        hour =  get_hour(event._parsed.rest)
        if hour:
            target += hour
    if not target or time.time() > target:
        event.reply("already passed given time.")
        return
    e = Event()
    e.txt = event.rest
    timer = Timer(target, e.reply, e.txt)
    launch(timer.start)
    event.reply("ok " +  time.ctime(target).replace("  ", " "))

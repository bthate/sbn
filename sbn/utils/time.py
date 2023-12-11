# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0718


"time related utilities"


import datetime
import re
import threading
import time as ttime


def __dir__():
    return (
        'NoDate',
        'day',
        'get_day',
        'get_hour',
        'get_time',
        'hms',
        'laps',
        'now',
        'parse_time',
        'to_date',
        'to_day',
        'to_time',
        'today',
        'year'
    )


__all__ = __dir__()


class NoDate(Exception):

    pass


year_formats = [
    "%Y-%m-%d",
    "%d-%m-%Y",
    "%d-%m",
    "%m-%d",
]


timere = re.compile('(\S+)\s+(\S+)\s+(\d+)\s+(\d+):(\d+):(\d+)\s+(\d+)')


bdmonths = ['Bo', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


monthint = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12 
}


def day():
    return str(datetime.datetime.today()).split()[0]


def extract_time(daystr):
    for format in year_formats:
        try:
            res = ttime.mktime(ttime.strptime(daystr, format))
        except:
            res = None
        if res:
            return res


def file_time(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp)).replace(" ", os.sep) + "." + str(random.randint(111111,999999))


def get_day(daystr):
    try:
        ymdre = re.search('(\d+)-(\d+)-(\d+)', daystr)
        (day, month, year) = ymdre.groups()
    except:
        try:
            ymre = re.search('(\d+)-(\d+)', daystr)
            (day, month) = ymre.groups()
            year = ttime.strftime("%Y", ttime.localtime())
        except: raise ENODATE(daystr)
    day = int(day)
    month = int(month)
    year = int(year)
    date = "%s %s %s" % (day, bdmonths[month], year)
    return ttime.mktime(ttime.strptime(date, "%d %b %Y"))


def get_hour(daystr):
    try:
        hmsre = re.search('(\d+):(\d+):(\d+)', str(daystr))
        hours = 60 * 60 * (int(hmsre.group(1)))
        hoursmin = hours  + int(hmsre.group(2)) * 60
        hms = hoursmin + int(hmsre.group(3))
    except AttributeError:
        pass
    except ValueError:
        pass
    try:
        hmre = re.search('(\d+):(\d+)', str(daystr))
        hours = 60 * 60 * (int(hmre.group(1)))
        hms = hours + int(hmre.group(2)) * 60
    except AttributeError:
        return 0
    except ValueError:
        return 0
    return hms


def get_time(txt):
    try:
        target = get_day(txt)
    except ENODATE:
        target = to_day(day())
    hour =  get_hour(txt)
    if hour:
        target += hour
    return target


def hms():
    return str(datetime.datetime.today()).split()[1].split(".")[0]


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
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def now():
    return str(datetime.datetime.now())


def parse_time(txt):
    seconds = 0
    target = 0
    txt = str(txt)
    for word in txt.split():
        if word.startswith("+"):
            seconds = int(word[1:])
            return ttime.time() + seconds
        if word.startswith("-"):
            seconds = int(word[1:])
            return ttime.time() - seconds
    if not target:
        try:
            target = get_day(txt)
        except ENODATE:
            target = to_day(day())
        hour =  get_hour(txt)
        if hour:
            target += hour
    return target


def to_date(*args, **kwargs):
    date = args[0]
    if not date:
        return None
    date = date.replace("_", ":")
    res = date.split()
    ddd = ""
    try:
        if "+" in res[3]:
            raise ValueError
        if "-" in res[3]:
            raise ValueError
        int(res[3])
        ddd = "{:4}-{:#02}-{:#02} {:6}".format(res[3], monthint[res[2]], int(res[1]), res[4])
    except (IndexError, KeyError, ValueError):
        try:
            if "+" in res[4]:
                raise ValueError
            if "-" in res[4]:
                raise ValueError
            int(res[4])
            ddd = "{:4}-{:#02}-{:02} {:6}".format(res[4], monthint[res[1]], int(res[2]), res[3])
        except (IndexError, KeyError, ValueError):
            try:
                ddd = "{:4}-{:#02}-{:02} {:6}".format(res[2], monthint[res[1]], int(res[0]), res[3])
            except (IndexError, KeyError):
                try:
                    ddd = "{:4}-{:#02}-{:02}".format(res[2], monthint[res[1]], int(res[0]))
                except (IndexError, KeyError):
                    try:
                        ddd = "{:4}-{:#02}".format(res[2], monthint[res[1]])
                    except (IndexError, KeyError):
                        try:
                            ddd = "{:4}".format(res[2])
                        except (IndexError, KeyError):
                            ddd = ""
    return ddd.replace(":", "_")


def to_day(daystr):
    previous = ""
    line = ""
    daystr = str(daystr)
    for word in daystr.split():
        line = previous + " " + word
        previous = word
        try:
            res = extract_time(line.strip())
        except ValueError:
            res = None
        if res:
            return res
        line = ""


def to_time(daystr):
    daystr = str(daystr)
    daystr = daystr.split(".")[0]
    daystr = daystr.replace("GMT", "")
    daystr = daystr.replace("_", ":")
    daystr = " ".join([x.capitalize() for x in daystr.split() if not x[0] in ["+", "-"]])
    res = 0
    try: res = ttime.mktime(ttime.strptime(daystr, "%a, %d %b %Y %H:%M:%S"))
    except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%a, %d %b %Y %H:%M:%S %z"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%a, %d %b %Y %H:%M:%S %z"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%a %d %b %H:%M:%S %Y"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%a %d %b %H:%M:%S %Y %z"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%Y-%m-%d %H:%M:%S"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%d-%m-%Y %H:%M:%S"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%d-%m-%Y %H:%M"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%Y-%m-%d %H:%M"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%Y-%m-%d"))
        except: pass
    if not res:
        try: res = ttime.mktime(ttime.strptime(daystr, "%d-%m-%Y"))
        except: pass
    if not res: raise ENODATE(daystr)
    return res


def today():
    t = rtime().split(".")[0]
    ttime = ttime.strptime(t, "%Y-%m-%d/%H:%M:%S")
    result = ttime.mktime(ttime)
    return result


def year():
    return str(datetime.datetime.now().year)

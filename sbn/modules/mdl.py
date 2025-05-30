# This file is placed in the Public Domain.


"Genocide model of the Netherlands since 4 March 2019."


import datetime
import time


from .. import Object, construct, keys
from .. import Event, Fleet, Repeater
from .  import debug, elapsed


DAY = 24*60*60
YEAR = 365*DAY
SOURCE = "https://github.com/bthate/genocide"
STARTDATE = "2019-03-04 00:00:00"
STARTTIME = time.mktime(time.strptime(STARTDATE, "%Y-%m-%d %H:%M:%S"))


def init():
    for key in keys(oorzaken):
        if "Psych" not in key:
            continue
        val = getattr(oorzaken, key, None)
        if val and int(val) > 10000:
            evt = Event()
            evt.txt = ""
            evt.rest = key
            sec = seconds(val)
            name = aliases.get(key)
            repeater = Repeater(sec, cbstats, evt, thrname=name)
            repeater.start()
            debug(f"{name} at {STARTDATE} {elapsed(time.time()-STARTTIME)}")



"model"


oor = """"Totaal onderliggende doodsoorzaken (aantal)";
         "1 Infectieuze en parasitaire ziekten/Totaal infectieuze en parasitaire zktn (aantal)";
         "1 Infectieuze en parasitaire ziekten/1.1 Tuberculose (aantal)";
         "1 Infectieuze en parasitaire ziekten/1.2 Meningokokkeninfecties (aantal)";
         "1 Infectieuze en parasitaire ziekten/1.3 Virale hepatitis (aantal)";
         "1 Infectieuze en parasitaire ziekten/1.4 AIDS (aantal)";
         "1 Infectieuze en parasitaire ziekten/1.5 Ov. infectieuze en parasitaire zktn (aantal)";
         "2 Nieuwvormingen/Totaal nieuwvormingen (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/Totaal kwaadaardige nieuwvormingen (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.1 Kw. nv. van lip, mond en keel (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.2 Kw. nv. van slokdarm (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.3 Kw. nv. van maag (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.4 Kw. nv. van dikke darm (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.5 Kw. nv. van endeldarm en anus (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.6 Kw. nv. lever en intrah. galwegen (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.7 Kw. nv. van galblaas en galwegen (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.8 Kw. nv. van alvleesklier (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.9 Kw. nv. van strottenhoofd (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.10 Kw. nv. van luchtpijp en long (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.11 Melanoom van huid (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.12 Kw. nv. van borst (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.13 Kw. nv. van baarmoederhals (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.14 Kw. nv. van baarmoederlichaam (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.15 Kw. nv. van eierstok (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.16 Kw. nv. van prostaat (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.17 Kw. nv. nier, behalve nierbekken (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.18 Kw. nv. van urineblaas (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.19 Kw. nv. lymf. en bloedv. weefsel (aantal)";
         "2 Nieuwvormingen/2.1 Kwaadaardige nieuwvormingen/2.1.20 Ov. kwaadaardige nieuwvormingen (aantal)";
         "2 Nieuwvormingen/2.2 Overige nieuwvormingen (aantal)";
         "3 Zktn bloed, bloedvormende organen en.. (aantal)";
         "4 Endocriene, voedings-, stofwiss. zktn/Totaal endocriene, voedings-, stofwiss.. (aantal)";
         "4 Endocriene, voedings-, stofwiss. zktn/4.1 Suikerziekte (aantal)";
         "4 Endocriene, voedings-, stofwiss. zktn/4.2 Ov. endocriene, voedings-, stofwis.. (aantal)";
         "5 Psychische en gedragsstoornissen/Totaal psychische stoornissen (aantal)";
         "5 Psychische en gedragsstoornissen/5.1 Psychische stoornissen door alcohol (aantal)";
         "5 Psychische en gedragsstoornissen/5.2 Psychische stoornissen drugs en vl.. (aantal)";
         "5 Psychische en gedragsstoornissen/5.3 Overige psychische stoornissen (aantal)";
         "6 Ziekten van zenuwstelsel en zintuigen/Totaal ziekten zenuwstelsel en zintuigen (aantal)";
         "6 Ziekten van zenuwstelsel en zintuigen/6.1 Hersenvliesontsteking (aantal)";
         "6 Ziekten van zenuwstelsel en zintuigen/6.2 Ziekte van Parkinson (aantal)";
         "6 Ziekten van zenuwstelsel en zintuigen/6.3 Ov. zktn zenuwstelsel en zintuigen (aantal)";
         "7 Ziekten van hart en vaatstelsel/Totaal ziekten van hart en vaatstelsel (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.1 Ziekten van de kransvaten/Totaal ziekten van de kransvaten (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.1 Ziekten van de kransvaten/7.1.1 Acuut hartinfarct (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.1 Ziekten van de kransvaten/7.1.2 Overige ziekten van de kransvaten (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.2 Overige hartziekten (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.3 Hersenvaatletsels (aantal)";
         "7 Ziekten van hart en vaatstelsel/7.4 Overige ziekten hart en vaatstelsel (aantal)";
         "8 Ziekten van de ademhalingsorganen/Totaal ziekten van de ademhalingsorganen (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.1 Griep (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.2 Longontsteking (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.3 Chron. aand. onderste luchtwegen/Totaal chronische aand. onderste lucht.. (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.3 Chron. aand. onderste luchtwegen/8.3.1 Astma (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.3 Chron. aand. onderste luchtwegen/8.3.2 Ov. chron. aand. onderste luchtw.. (aantal)";
         "8 Ziekten van de ademhalingsorganen/8.4 Overige ziekten ademhalingsorganen (aantal)";
         "9 Ziekten van de spijsverteringsorganen/Totaal ziekten spijsverteringsorganen (aantal)";
         "9 Ziekten van de spijsverteringsorganen/9.1 Maagzweer en zweer aan twaalfvinge.. (aantal)";
         "9 Ziekten van de spijsverteringsorganen/9.2 Chronische leveraandoeningen/Totaal chronische leveraandoeningen (aantal)";
         "9 Ziekten van de spijsverteringsorganen/9.2 Chronische leveraandoeningen/9.2.1 Chronische leveraand. alcohol (aantal)";
         "9 Ziekten van de spijsverteringsorganen/9.2 Chronische leveraandoeningen/9.2.2 Ov. chronische leveraandoeningen (aantal)";
         "9 Ziekten van de spijsverteringsorganen/9.3 Ov. ziekten spijsverteringsorganen (aantal)";
         "10 Ziekten van huid en subcutis (aantal)";
         "11 Ziekten botspierstelsel en bindweef../Totaal ziekten spieren, beend., bindwfsl (aantal)";
         "11 Ziekten botspierstelsel en bindweef../11.1 Reumatoïde artritis en artrose (aantal)";
         "11 Ziekten botspierstelsel en bindweef../11.2 Ov. zktn spieren, beend., bindwfsl (aantal)";
         "12 Ziekten van urogenitaal stelsel/Totaal zktn urinewegen en gesl. organen (aantal)";
         "12 Ziekten van urogenitaal stelsel/12.1 Ziekten van nier en urineleider (aantal)";
         "12 Ziekten van urogenitaal stelsel/12.2 Ov. zktn urinewegen en gesl.organen (aantal)";
         "13 Zwangerschap, bevalling en kraambed. (aantal)";
         "14 Aandoeningen v.d. perinatale periode (aantal)";
         "15 Aangeboren afwijkingen/Totaal aangeboren afwijkingen (aantal)";
         "15 Aangeboren afwijkingen/15.1 Aangeboren afw. zenuwstelsel (aantal)";
         "15 Aangeboren afwijkingen/15.2 Aangeboren afw. hart en bloedvaten (aantal)";
         "15 Aangeboren afwijkingen/15.3 Overige aangeboren afwijkingen (aantal)";
         "16 Sympt., afwijkende klinische bevind../Totaal symp. en onvoll. omschr. ziekte.. (aantal)";
         "16 Sympt., afwijkende klinische bevind../16.1 Wiegendood (aantal)";
         "16 Sympt., afwijkende klinische bevind../16.2 Onvoll. omschr. en onbek. oorzaken (aantal)";
         "16 Sympt., afwijkende klinische bevind../16.3 Ov. symptomen en onvolledig omsch.. (aantal)";
         "17 Uitwendige doodsoorzaken/Totaal uitwendige doodsoorzaken (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/Totaal ongevallen (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.1 Vervoersongevallen/Totaal vervoersongevallen (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.1 Vervoersongevallen/17.1.1.1 Wegverkeersongevallen (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.1 Vervoersongevallen/17.1.1.2 Overige vervoersongevallen (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.2 Accidentele val (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.3 Accidentele verdrinking (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.4 Accidentele vergiftiging (aantal)";
         "17 Uitwendige doodsoorzaken/17.1 Ongevallen/17.1.5 Overige ongevallen (aantal)";
         "17 Uitwendige doodsoorzaken/17.2 Zelfdoding (aantal)";
         "17 Uitwendige doodsoorzaken/17.3 Moord en doodslag (aantal)";
         "17 Uitwendige doodsoorzaken/17.4 Gebeurtenissen opzet onbekend (aantal)";
         "17 Uitwendige doodsoorzaken/17.5 Overige uitwendige doodsoorzaken (aantal)";
         "18 COVID-19 (Coronavirus ziekte 19)/18 Totaal COVID-19 (Coronavirus 19) (aantal)";
         "18 COVID-19 (Coronavirus ziekte 19)/18.1 Vastgestelde COVID-19 (aantal)";
         "18 COVID-19 (Coronavirus ziekte 19)/18.2 Vermoedelijke COVID-19 (aantal)""".split(";")


aantal = """
          168678;
          2974;
          32;
          1;
          34;
          23;
          2884;
          47089;
          45103;
          690;
          2013;
          1150;
          3395;
          1235;
          956;
          452;
          2942;
          205;
          10080;
          811;
          3083;
          230;
          560;
          1032;
          3006;
          923;
          1359;
          3636;
          7345;
          1986;
          560;
          3646;
          2799;
          847;
          11682;
          531;
          61;
          11090;
          8387;
          50;
          1792;
          6545;
          36622;
          8037;
          4718;
          3319;
          12682;
          8850;
          7053;
          10503;
          295;
          2726;
          5776;
          146;
          5630;
          1706;
          4882;
          138;
          948;
          433;
          515;
          3796;
          323;
          1067;
          333;
          734;
          3248;
          1958;
          1290;
          2;
          390;
          436;
          42;
          87;
          307;
          7664;
          11;
          4436;
          3217;
          9030;
          6433;
          633;
          590;
          43;
          5234;
          107;
          238;
          221;
          1823;
          107;
          28;
          639;
          20173;
          17495;
          2678
         """.split(";")


aliases = {}
aliases["Nieuwvormingen"] = "cancer"
aliases["Hart en vaatstelsel"] = "hart"
aliases["Psychische en gedragsstoornissen"] = "mental"
aliases["Ademhalingsorganen"] = "breathing"
aliases["Uitwendige doodsoorzaken"] = "externals"
aliases["Zenuwstelsel en zintuigen"] = "nerves"
aliases["Afwijkende klinische bevindingen"] = "NOS"
aliases["Spijsverteringsorganen"] = "stomach"
aliases["Endocriene, voedings-, stofwisseling"] = "metabolism"
aliases["Urogenitaal stelsel"] = "kidney"
aliases["Infectieuze en parasitaire ziekten"] = "infectious"
aliases["Botspierstelsel en bindweefsel"] = "muscle"
aliases["Bloed, bloedvormende organen"] = "blood"
aliases["Aangeboren afwijkingen"] = "birth"
aliases["Huid en subcutis"] = "skin"
aliases["Zwangerschap"] = "pregnancy"
aliases["Suicide"] = "suicide"


demo = Object()
demo.gehandicapten = 2000000
demo.ggz = 800000
demo.population = 17440000
demo.part = 7000000000 / demo.population


jaar = {}
jaar["WvGGZ"] = 14206
jaar["Pvp"] = 20088
jaar["Wzd"] = 25000
jaar["Wfz"] = 23820
jaar["totaal"] = 168678


oorzaak = Object()
construct(oorzaak, zip(oor, aantal))
oorzaken = Object()


"utilities"


def getalias(txt):
    result = ""
    for key, value in aliases.items():
        if txt.lower() in key.lower():
            result = value
            break
    return result

def getday():
    day = datetime.datetime.now()
    day = day.replace(hour=0, minute=0, second=0, microsecond=0)
    return day.timestamp()


def getnr(nme):
    for k in keys(oorzaken):
        if nme.lower() in k.lower():
            return int(getattr(oorzaken, k))
    return 0


def seconds(nrs):
    if not nrs:
        return nrs
    return 60*60*24*365 / float(nrs)


def iswanted(k, line):
    for word in line:
        if word in k:
            return True
    return False


def daily():
    while 1:
        time.sleep(24*60*60)
        evt = Event()
        cbnow(evt)


def hourly():
    while 1:
        time.sleep(60*60)
        evt = Event()
        cbnow(evt)


"callbacks"


def cbnow(_evt):
    delta = time.time() - STARTTIME
    txt = elapsed(delta) + " "
    for nme in sorted(keys(oorzaken), key=lambda x: seconds(getnr(x))):
        needed = seconds(getnr(nme))
        if needed > 60*60:
            continue
        nrtimes = int(delta/needed)
        txt += f"{getalias(nme)} {nrtimes} | "
    txt += "https://pypi.org/project/genocide"
    Fleet.announce(txt)


def cbstats(evt):
    nme = evt.rest or "Psych"
    needed = seconds(getnr(nme))
    if needed:
        delta = time.time() - STARTTIME
        nrtimes = int(delta/needed)
        nryear = int(YEAR/needed)
        nrday = int(DAY/needed)
        delta2 = time.time() - getday()
        thisday = int(delta2/needed)
        txt = "%s %s #%s (%s/%s/%s) every %s" % (
            elapsed(delta),
            getalias(nme).upper(),
            nrtimes,
            thisday,
            nrday,
            nryear,
            elapsed(needed)
        )
        Fleet.announce(txt)


"commands"


def dis(event):
    delta = time.time() - STARTTIME
    txt = elapsed(delta) + " "
    for nme in sorted(keys(oorzaken), key=lambda x: seconds(getnr(x))):
        needed = seconds(getnr(nme))
        if needed > 60*60:
            continue
        nrtimes = int(delta/needed)
        txt += f"{getalias(nme)} {nrtimes} | "
    txt += "https://pypi.org/project/genocide"
    event.reply(txt)


def now(event):
    nme = event.rest or "Psych"
    needed = seconds(getnr(nme))
    if needed:
        delta = time.time() - STARTTIME
        nrtimes = int(delta/needed)
        nryear = int(YEAR/needed)
        nrday = int(DAY/needed)
        thisday = int(DAY % needed)
        txt = "%s %s #%s (%s/%s/%s) every %s" % (
            elapsed(delta),
            getalias(nme),
            nrtimes,
            thisday,
            nrday,
            nryear,
            elapsed(needed)
        )
        event.reply(txt)


"init"


def boot():
    _nr = -1
    for key in keys(oorzaak):
        _nr += 1
        if _nr == 0:
            continue
        if key.startswith('"'):
            key = key[1:]
        lines = key.split("/")
        if len(lines) > 1 and not lines[1].startswith("Totaal"):
            continue
        atl = lines[0].replace('(aantal)"', "")
        atl = atl.replace("Ziekten van de", "")
        atl = atl.replace("Ziekten van", "")
        atl = atl.replace("Ziekten", "")
        atl = atl.replace("Zktn", "")
        atl = atl.replace("zktn", "")
        atl = atl.replace("en..", "")
        atl = atl.replace("..", "")
        atl = atl.replace("bindweef", "bindweefsel")
        atl = atl.replace("bevind", "bevindingen")
        atl = atl.replace("stofwiss.", "stofwisseling")
        atl = atl.replace("Sympt.,", "")
        atl = atl.replace(", bevalling en kraambed. ", "")
        atl = atl.replace("Aandoeningen v.d. ", "")
        nms = " ".join(atl.split()[1:]).capitalize()
        nms = nms.strip()
        setattr(oorzaken, nms, aantal[_nr])


boot()

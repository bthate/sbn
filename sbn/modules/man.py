# This file is placed in the Public Domain
#
# pylint: disable=C0116


"""NAME


    LIBBOT - library to program bots


DESCRIPTION


    LIBBOT is a python3 IRC bot intended to be programmable in a
    static, only code, no popen, no user imports and no reading
    modules from a directory, way. 

    LIBBOT provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text.


SYNOPSIS


    bot <cmd> [key=val] 
    bot <cmd> [key==val]
    bot [-c] [-d] [-v] [-i]


INSTALL


    $ pipx install bot


USAGE


    list of commands

    $ bot cmd
    cmd,err,flt,sts,thr,upt

    start a console

    $ bot -c
    >

    start additional modules

    $ bot -c mod=<mod1,mod2>
    >

    list of modules

    $ bot mod
    bsc,err,flt,irc,log,man,mod,rss,shp,
    sts,tdo,thr,udp

    to start irc, add mod=irc when
    starting

    $ bot -ci mod=irc

    to start rss, also add mod=rss
    when starting

    $ bot -ci mod=irc,rss

    start as daemon

    $ bot -d mod=irc,rss
    $ 


CONFIGURATION


    irc

    $ bot cfg server=<server>
    $ bot cfg channel=<channel>
    $ bot cfg nick=<nick>

    sasl

    $ bot pwd <nsvnick> <nspass>
    $ bot cfg password=<frompwd>

    rss

    $ bot rss <url>
    $ bot dpl <url> <item1,item2>
    $ bot rem <url>
    $ bot nme <url< <name>


COMMANDS


    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    slg - slogan
    thr - show the running threads


SYSTEMD


    replace <user> with the username giving the pipx command.

    [Unit]
    Description=the complete
    Requires=network.target
    After=network.target

    [Service]
    DynamicUser=True
    Type=forking
    User=<user>
    Group=<uer>
    PIDFile=bot.pid
    WorkingDirectory=/home/<user>/.bot
    ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/bot -d mod=irc,rss
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target


FILES


    ~/.local/bin/bot
    ~/.local/pipx/venvs/bot/


AUTHOR


    botlib <botlib@proton.me>


COPYRIGHT


    BOT is placed in the Public Domain.


"""


def man(event):
    event.reply(__doc__)
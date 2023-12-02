.. _manual:


.. raw:: html

    <br><br>


.. title:: Manual


NAME

::

    SBN - Skull, Bones and Number (OTP-CR-117/19)


SYNOPSIS

::

    sbn <cmd> [key=val] 
    sbn <cmd> [key==val]
    sbn [-c] [-v]


DESCRIPTION

::


    SBN holds evidence that king netherlands is doing a genocide, a
    written response where king netherlands confirmed taking note of 
    “what i have written”, namely proof that medicine he uses in
    treatement laws like zyprexa, haldol, abilify and clozapine are
    poison that make impotent, is both physical (contracted muscles)
    and mental (make people hallucinate) torture and kills members
    of the victim groups. 

    SBN contains correspondence with the International Criminal Court,
    asking for arrest of the king of the netherlands, for the genocide
    he is committing with his new treatement laws. Current status is
    "no basis to proceed" judgement of the prosecutor which requires a
    "basis to prosecute" to have the king actually arrested.


INSTALL


::

    $ pipx install sbn


USAGE

::

    without any argument the bot does nothing

    $ sbn
    $

    giving an argument makes the bot check for a command

    see list of commands

    $ sbn cmd
    cfg,cmd,dlt,dne,dpl,log,man,met,mod,mre,nme,now,pwd
    rem,req,rss,sts,tdo,thr

    start a console

    $ sbn -c
    >

    list of modules

    $ sbn mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr


    use -v for verbose


    $ sbn -cv
    SBN started CV started Sat Dec 2 17:53:24 2023
    >

    start daemon

    $ sbnd
    $ 

    show request to the prosecutor

    $ sbn req
    Information and Evidence Unit
    Office of the Prosecutor
    Post Office Box 19519
    2500 CM The Hague
    The Netherlands
    

CONFIGURATION


::

    irc

    $ sbn cfg server=<server>
    $ sbn cfg channel=<channel>
    $ sbn cfg nick=<nick>

    sasl

    $ sbn pwd <nsvnick> <nspass>
    $ sbn cfg password=<frompwd>

     rss

    $ sbn rss <url>
    $ sbn dpl <url> <item1,item2>
    $ sbn rem <url>
    $ sbn nme <url< <name>


COMMANDS


::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    thr - show the running threads


SYSTEMD


::

    replace "<user>" with the user running pipx


    [Unit]
    Description=Skull, Bones and Number (OTP-CR-117/19)
    Requires=network.target
    After=network.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.sbn
    ExecStart=/home/<user>/.local/pipx/venvs/sbn/bin/sbnd

    [Install]
    WantedBy=multi-user.target


    if you don't have a ~/.sbn directory you need to create it


    $ mkdir ~/.sbn


    then run this


    $ sudo systemctl enable sbn --now


    default channel/server is #rssbot on localhost


FILES

::

    ~/.local/bin/sbn
    ~/.local/pipx/venvs/sbn/


AUTHOR


::

    Bart Thate <bthate@dds.nl>


COPYRIGHT


::

    SBN is Public Domain.

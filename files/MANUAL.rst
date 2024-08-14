README
######


**NAME**

::

   ``sbn`` - Skull, Bones and Number (SBN)


**SYNOPSIS**

::

    sbn <cmd> [key=val] [key==val]
    sbnc [-a] [-i] [-v]
    sbnd


**DESCRIPTION**


``SBN`` holds evidence that king netherlands
is doing a genocide, a written response
where king netherlands confirmed taking note
of “what i have written”, namely proof that
medicine he uses in treatement laws like
zyprexa, haldol, abilify and clozapine are
poison that make impotent, is both physical
(contracted muscles) and mental (make people
hallucinate) torture and kills members of the
victim groups.

``SBN`` contains correspondence with the
International Criminal Court, asking for the
arrest of king netherlands, for the genocide
he is committing with his new treatement laws.

Current status is a "no basis to proceed"
judgement of the prosecutor which requires
a "basis to prosecute" to have the king
actually arrested and, thereby, his genocide
stopped.


INSTALL

::

    $ pipx install sbn
    $ pipx ensurepath

    <new terminal>

    $ nixt srv > sbn.service
    $ sudo mv sbn.service /etc/systemd/system/
    $ sduo systemctl enable sbn --now

    joins #sbn on localhost


**USAGE**

without any argument the bot does nothing::

    $ sbn
    $

see list of commands::

    $ sbn cmd
    cmd,dne,err,log,mod,req,tdo,thr,tmr

start a console::

    $ sbnc
    >

use -i to run init on modules::

    $ sbnc -ai

start daemon::

    $ sbnd


show request to the prosecutor::

    $ sbn req
    Information and Evidence Unit
    Office of the Prosecutor
    Post Office Box 19519
    2500 CM The Hague
    The Netherlands


**CONFIGURATION**

irc::

    $ sbn cfg server=<server>
    $ sbn cfg channel=<channel>
    $ sbn cfg nick=<nick>

sasl::

    $ sbn pwd <nsvnick> <nspass>
    $ sbn cfg password=<frompwd>

rss::

    $ sbn rss <url>
    $ sbn dpl <url> <item1,item2>
    $ sbn rem <url>
    $ sbn nme <url> <name>

opml::

    $ sbn imp <filename>
    $ sbn exp


**OPTIONS**

here is a list of commandline options ``sbn`` provides::

    -a     load all modules
    -i     start services
    -v     use verbose


**COMMANDS**

commands are mostely for irc and rss management::

    cfg - irc configuration
    cmd - commands
    dlt - remove a user
    dpl - sets display items
    exp - export opml
    fnd - find objects 
    imp - import opml
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - request 
    rss - add a feed
    thr - show the running threads


**FILES**

pipx stores the ``sbn`` documentation in it;s local pipx environment::

    ~/.sbn
    ~/.local/bin/sbn
    ~/.local/bin/sbnc
    ~/.local/bin/sbnd
    ~/.local/pipx/venvs/sbn/*


**AUTHOR**

I am reachable at the following email::

    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

::

    SBN is Public Domain.

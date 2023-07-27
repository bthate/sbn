# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"parser"


def __dir__():
    return (
            "parse",
           )


def parse(self, txt=None) -> None:
    self.args = self.args or []
    self.cmd = self.cmd or""
    self.gets = self.gets or {}
    self.mod = self.mod or ""
    self.opts = self.opts or ""
    self.sets = self.sets or {}
    self.otxt = txt or ""
    for spli in self.otxt.split():
        if spli.startswith("-"):
            try:
                self.index = int(spli[1:])
            except ValueError:
                self.opts += spli[1:]
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                self.mod += f",{value}"
                continue
            self.sets[key] = value
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            self.gets[key] = value
            continue
        if not self.cmd:
            self.cmd = spli
            continue
        self.args.append(spli)
    self.txt = self.cmd or ""
    if self.args:
        self.rest = str(" ".join(self.args))
        if self.rest:
            self.txt += " " + self.rest

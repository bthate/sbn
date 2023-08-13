# This file is placed in the Public Domain.
#
# pylint: disable=C0116,E0402


"available modules"


import os


from .. import modules


def __dir__():
    return (
            "mod",
           )


def mod(event):
    path = modules.__path__[0]
    modlist = [
               x[:-3] for x in os.listdir(path)
               if x.endswith(".py")
               and x not in ["__main__.py", "__init__.py"]
              ]
    event.reply(",".join(sorted(modlist)))

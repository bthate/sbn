# This file is placed in the Public Domain.
#
# pylint: disable=C0115,E0402


"main"


from .runtime import wrap, main


if __name__ == "__main__":
    wrap(main)

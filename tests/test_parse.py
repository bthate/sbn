# This file is placed in the Public Domain.
#
# pylint: disable=C0114,C0115,C0116,W0703,C0413
# pylama: ignore=E402


"parsing"


import unittest


from sbn.clients import parse
from sbn.objects import Default
from sbn.storage import prt


class TestDecoder(unittest.TestCase):

    def test_parse(self):
        prs = Default()
        parse(prs, "cmd")
        self.assertEqual(prs["cmd"], "cmd")

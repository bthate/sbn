# This file is placed in the Public Domain.


"static tables"


import unittest


from sbn.statics import NAMES


class TestStatic(unittest.TestCase):

    def test_names(self):
        self.assertTrue(NAMES)

# This file is placed in the Public Domain.


"engine"


import unittest


from sbn.handler import Handler


class TestHandler(unittest.TestCase):

    def testcomposite(self):
        eng = Handler()
        self.assertEqual(type(eng), Handler)

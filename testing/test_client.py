# This file is placed in the Public Domain.


"clients"


import unittest


from sbn.clients import Client
from sbn.handler import Event


def hello(event):
    event.reply("hello")
    event.ready()


clt = Client()
clt.register("hello", hello)
clt.start()


class TestHandler(unittest.TestCase):

    def test_loop(self):
        e = Event()
        e.type = "hello"
        clt.put(e)
        e.wait()
        self.assertTrue(True)

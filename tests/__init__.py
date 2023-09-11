# This file is placed in the Public Domain.
#
#


"unittest"

import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


import sbn


sbn.storage.Storage.workdir = ".test"

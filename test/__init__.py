# This file is placed in the Public Domain.
#
#


"unittest"

import os
import sys


sys.path.insert(0, "lib")


from sbn.storage import Storage


Storage.workdir = ".test"

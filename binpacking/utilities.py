from __future__ import print_function

import os
from builtins import str
from past.builtins import basestring


def print_binsizes(bins,weight_column):
    print("=== distributed items to bins with sizes ===")
    formatstr = "%0" + str(len(str(len(bins)-1))) + "d"
    for ib,b in enumerate(bins):
        print(formatstr % ib, sum([t[weight_column] for t in b]))
    
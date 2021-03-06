"""
Various globals and constants used through the application
"""

import argparse

SWITCHES: argparse.Namespace = argparse.Namespace()

CONFIG: argparse.Namespace = argparse.Namespace()

TIMEOUT_DISPLAY_LIST = [["10 sec", 10]]
for n in range(1, 13):
    TIMEOUT_DISPLAY_LIST.append([str(n * 10) + " min", n * 600])


holdSec = 20
continueSec = 20

lastClueNumber = 0
teamStatusDict = {}

"""
Various globals and constants used through the application
"""

TIMEOUT_DISPLAY_LIST = [["10 sec", 10]]
for n in range(1, 13):
    TIMEOUT_DISPLAY_LIST.append([str(n * 10) + " min", n * 600])


holdSec = 20
continueSec = 20

teamStatusDict = {}


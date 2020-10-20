import logging
from enum import IntEnum

LOG = logging.getLogger("main")


class StatusCode(IntEnum):
    """Enumeration of the status codes for teams."""
    AT_IC = 1
    AVAILABLE = 2
    IN_TRANSIT = 3
    WORKING = 4
    STANDBY = 5
    WAITING_FOR_TRANSPORT = 6
    RESTING = 7
    OFF_DUTY = 8

    @classmethod
    def possibleValues(cls) -> str:
        return ", ".join([e.name for e in cls])

    @classmethod
    def displayNames(cls):
        return {
            cls.AT_IC: "At Command Post",
            cls.AVAILABLE: "Available",
            cls.IN_TRANSIT: "In Transit",
            cls.WORKING: "Working",
            cls.STANDBY: "STANDBY",
            cls.WAITING_FOR_TRANSPORT: "Waiting for Transport",
            cls.RESTING: "Resting",
            cls.OFF_DUTY: "Off Duty"
        }

    def displayName(self) -> str:
        return StatusCode.displayNames()[self]

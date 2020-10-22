import logging
import enum

LOG = logging.getLogger("main")


@enum.unique
class StatusCode(enum.IntEnum):
    """
    Enumeration of the team's statuses.
    This list includes actual physical statuses (WORKING, STANDBAY) as well as
    meta statuses (TIMED_OUT_ORANGE, UNCHANGED).
    All of these serve as indexes into the styling dictionary (below), but
    the teams can only be assigned the non-meta statuses.
    """
    UNKNOWN = 0
    AT_IC = 1
    AVAILABLE = 2
    IN_TRANSIT = 3
    WORKING = 4
    STANDBY = 5
    WAITING_FOR_TRANSPORT = 6
    RESTING = 7
    OFF_DUTY = 8
    TIMED_OUT_ORANGE = 9   # timed out at the first threshold
    TIMED_OUT_RED = 10     # timed out at the second threshold
    CALL_ATTENTION = 11    # not timed out, but needs to call attention anyway
    UNCHANGED = 99

    def __str__(self):
        return StatusCode._display_names.get(self)

    @classmethod
    def possible_values(cls) -> str:
        return ", ".join([e.name for e in cls])

    def display_name(self) -> str:
        return str(self)

    def encoding(self) -> str:
        """
        Returns the official encoding for the enumeration (when serializing anew).
        """
        return self.name

    def is_meta_status(self):
        """
        Returns true if the status is not one that is actually assignable to a team.
        """
        return self in [StatusCode.UNKNOWN, StatusCode.UNCHANGED, StatusCode.TIMED_OUT_ORANGE, StatusCode.TIMED_OUT_RED, StatusCode.CALL_ATTENTION]

    def requires_attention(self):
        """
        Returns true for statuses that require prompt attention (without having to time out first).
        """
        return self in [StatusCode.WAITING_FOR_TRANSPORT, StatusCode.STANDBY, StatusCode.AVAILABLE]

    def can_time_out(self):
        return (not self.is_meta_status()) and (self not in [StatusCode.AT_IC, StatusCode.OFF_DUTY])


# Ammend this class to add a constructor, one which takes a string with an
# "encoding" that gets translated to a corresponding enumeration.
# Each enumeration can have many possible encodings.
StatusCode.__new__ = lambda cls, value: (cls._encodings.get(value.upper(), StatusCode.UNKNOWN)
                                         if isinstance(value, str) else super(StatusCode, cls).__new__(cls, value))

StatusCode._display_names = {
    StatusCode.AT_IC: "At IC",
    StatusCode.AVAILABLE: "Available",
    StatusCode.IN_TRANSIT: "In Transit",
    StatusCode.WORKING: "Working",
    StatusCode.STANDBY: "STANDBY",
    StatusCode.WAITING_FOR_TRANSPORT: "Waiting for Transport",
    StatusCode.RESTING: "Resting",
    StatusCode.OFF_DUTY: "Off Duty",
    StatusCode.UNKNOWN: "(unknown)",
    StatusCode.UNCHANGED: "(unchanged)",
    StatusCode.TIMED_OUT_ORANGE: "Time-out Warning",
    StatusCode.TIMED_OUT_RED: "Timed Out",
    StatusCode.CALL_ATTENTION: "Call Attention",
}

# Initialze the encodings table with the enum names (the official encoding)
# Note: encodings are compared in upper case
StatusCode._encodings = {e.name: e for e in StatusCode}
# Add in the names without underscores
StatusCode._encodings.update({e.name.replace("_", " "): e for e in StatusCode})
# Add in a reverse lookup of the display names
StatusCode._encodings.update({val.upper(): key for key, val in StatusCode._display_names.items()})


STATUS_STYLE_DICT = {}
# even though tab labels are created with font-size:20px and the tab sizes and margins are created accordingly,
#  something after creation time is changing font-sizes to a smaller size.  So, just
#  hardcode them all here to force 20px always.
tab_font_size = "20px"

# Actual Statuses (assignable)
STATUS_STYLE_DICT[StatusCode.AT_IC] = f"font-size:{tab_font_size};background:#00ff00;border:1px outset black;padding-left:0px;padding-right:0px"
STATUS_STYLE_DICT[StatusCode.IN_TRANSIT] = f"font-size:{tab_font_size};background:blue;color:white;border:1px outset black;padding-left:0px;padding-right:0px"
STATUS_STYLE_DICT[StatusCode.WORKING] = f"font-size:{tab_font_size};background:none;border:1px outset black;padding-left:0px;padding-right:0px"
STATUS_STYLE_DICT[StatusCode.OFF_DUTY] = f"font-size:{tab_font_size};color:#aaaaaa;background:none;border:none;padding-left:0px;padding-right:0px"
STATUS_STYLE_DICT[StatusCode.AVAILABLE] = f"font-size:{tab_font_size};background:#00ffff;border:1px outset black;padding-left:0px;padding-right:0px;padding-top:-1px;padding-bottom:-1px"
STATUS_STYLE_DICT[StatusCode.WAITING_FOR_TRANSPORT] = f"font-size:{tab_font_size};background:blue;color:white;border:1px outset black;padding-left:0px;padding-right:0px;padding-top:-1px;padding-bottom:-1px"
STATUS_STYLE_DICT[StatusCode.STANDBY] = f"font-size:{tab_font_size};background:black;color:white;border:1px outset black;padding-left:0px;padding-right:0px;padding-top:-1px;padding-bottom:-1px"

# Meta Statuses (alternate styling)
STATUS_STYLE_DICT[StatusCode.CALL_ATTENTION] = f"font-size:{tab_font_size};background:none;padding-left:1px;padding-right:1px"
STATUS_STYLE_DICT[StatusCode.TIMED_OUT_ORANGE] = f"font-size:{tab_font_size};background:orange;border:1px outset black;padding-left:0px;padding-right:0px;padding-top:-1px;padding-bottom:-1px"
STATUS_STYLE_DICT[StatusCode.TIMED_OUT_RED] = f"font-size:{tab_font_size};background:red;border:1px outset black;padding-left:0px;padding-right:0px;padding-top:-1px;padding-bottom:-1px"


# Messages will be compared in all lower-case.
# Order is important. Place the most reliable determinations up front.
STATUS_PER_PHRASING = [
    (r"\b10-8\b", StatusCode.AVAILABLE),
    (r"\b10-10\b", StatusCode.OFF_DUTY),
    (r"\b10-97\b", StatusCode.WORKING),
    (r"(request\w* transport\w*|transport\w* request\w*)", StatusCode.WAITING_FOR_TRANSPORT),
    (r"(\bat|@|\bstart\w*) (sa|search|assignment)\b", StatusCode.WORKING),
    (r"(\bat|@|\bstart\w*) (cp|mcp|ic|staging|command|base)\b", StatusCode.AT_IC),
    (r"\b(complete\w*|finish\w*) (sa|search|assignment)\b", StatusCode.AVAILABLE),
    (r"\b(enroute|evac\w*|depart\w*|driving|moving)\b", StatusCode.IN_TRANSIT),
    (r"\b(stand\w* ?by|hold\w* position)\b", StatusCode.STANDBY),
    (r"\brequest\w* (deputy|ranger|leo|law|police|detective|investigator)", StatusCode.STANDBY),
    (r"\b(on break|resting|rest break)\b", StatusCode.RESTING),
]

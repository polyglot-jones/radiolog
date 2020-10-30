from app.logic.teams import TeamNameFormat
import logging
from pathlib import Path
from gwpycore import GWConfigParser, GlobalSettings

from app.db.file_management import determine_rotate_method
from app.logic.exceptions import RadioLogConfigSettingWarning
from app.logic.mapping import CoordFormat, Datum

LOG = logging.getLogger("main")
CONFIG = GlobalSettings("config")

DEFAULT_NAME = "Search and Rescue"
DEFAULT_LOGO = "radiolog_logo.jpg"
DEFAULT_CLUE_REPORT = "resources/clueReportFillable.pdf"
DEFAULT_TIMEOUT = 30
DEFAULT_WORKINGDIR = "testdata"
DEFAULT_SARSOFT_SERVER = "localhost"


def _as_datum(input: str) -> Datum:
    return Datum.__members__[input]


def _as_coordFormat(input: str) -> CoordFormat:
    return CoordFormat.__members__[input]


CUSTOM_CONVERTERS = {"datum": _as_datum, "coordformat": _as_coordFormat}


def __agency_section(parser):
    CONFIG.agencyName = DEFAULT_NAME
    CONFIG.logo = Path(DEFAULT_LOGO)
    CONFIG.callsign_prefix = "Team"
    CONFIG.team_name_format = TeamNameFormat.NUMERIC
    CONFIG.quick_text = ""
    CONFIG.keymap = ""
    if parser.has_section("agency"):
        CONFIG.agencyName = parser["agency"].gettext("name", CONFIG.agencyName)
        CONFIG.logo = parser["agency"].getpath("logo", CONFIG.logo)
        CONFIG.callsign_prefix = parser["agency"].gettext("callsign_prefix", CONFIG.callsign_prefix)
        CONFIG.team_name_format = TeamNameFormat(parser["agency"].gettext("team_name_format", CONFIG.team_name_format))
        CONFIG.quick_text = parser["agency"].gettext("quick_text", CONFIG.quick_text)
        CONFIG.keymap = parser["agency"].gettext("keymap", CONFIG.keymap)

    if not CONFIG.keymap:
        CONFIG.keymap = "" if CONFIG.team_name_format == TeamNameFormat.NUMERIC else CONFIG.team_name_format.encoding()


def __storage_section(parser):
    CONFIG.firstWorkingDir = Path(DEFAULT_WORKINGDIR)
    CONFIG.secondWorkingDir = None
    (CONFIG.rotateScript, CONFIG.rotateDelimiter) = determine_rotate_method()

    if parser.has_section("storage"):
        CONFIG.firstWorkingDir = parser["storage"].getpath("firstworkingdir", CONFIG.firstWorkingDir)
        CONFIG.secondWorkingDir = parser["storage"].getpath("secondworkingdir", CONFIG.secondWorkingDir)
        CONFIG.rotateScript = parser["storage"].gettext("rotateScript", CONFIG.rotateScript)
        CONFIG.rotateDelimiter = parser["storage"].gettext("rotateDelimiter", CONFIG.rotateDelimiter)


def __display_section(parser):
    CONFIG.timeoutMinutes = DEFAULT_TIMEOUT  # initial timeout interval (valid: 10..120 step 10)
    if parser.has_section("display"):
        CONFIG.timeoutMinutes = parser["display"].getint("timeoutminutes", CONFIG.timeoutMinutes)


def __tabgroups_section(parser):
    CONFIG.tabGroups = []
    if parser.has_section("tabgroups"):
        CONFIG.tabGroups = []
        for (tabName, tabRE) in parser["tabgroups"].items():
            CONFIG.tabGroups.append(tabRE)


def __reports_section(parser):
    CONFIG.clueReport = Path(DEFAULT_CLUE_REPORT)
    if parser.has_section("reports"):
        CONFIG.clueReport = parser["reports"].getpath("cluereport", CONFIG.clueReport)


def __mapping_section(parser, issues):
    CONFIG.datum = Datum.WGS84
    CONFIG.coordFormat = CoordFormat.UTM7
    if parser.has_section("mapping"):
        try:
            CONFIG.datum = parser["mapping"].getdatum("datum", CONFIG.datum)
        except KeyError as e:
            issues.append(RadioLogConfigSettingWarning("[mapping]datum", e.args[0], Datum.possibleValues()))

        try:
            CONFIG.coordFormat = parser["mapping"].getcoordformat("coordformat", CONFIG.coordFormat)
        except KeyError as e:
            issues.append(RadioLogConfigSettingWarning("[mapping]coordformat", e.args[0], CoordFormat.possibleValues()))


def __interop_section(parser, issues):
    CONFIG.sarsoftServerName = DEFAULT_SARSOFT_SERVER
    if parser.has_section("interop"):
        CONFIG.sarsoftServerName = parser["RadioLog"].gettext("server", CONFIG.sarsoftServerName)


def __further_initialization():
    CONFIG.lastClueNumber = 0


def load_config(filename: str = "", ini: str = ""):
    """
    Parse the contents of the config (INI) file.

    Args:
      filename -- the name of the file to be parsed, or...
      ini -- the actual text to be parsed
      config (optional) -- An existing argparse.Namespace to be appended to

    Returns:
      An object of type argparse.Namespace. Access the settings as object attributes (e.g. CONFIG.datum).
    """
    LOG.trace("Loading config")
    parser = GWConfigParser(converters=CUSTOM_CONVERTERS)
    if filename:
        parser.parse_file(Path(filename))
    else:
        parser.read_string(ini)

    issues = []
    __agency_section(parser)
    __display_section(parser)
    __tabgroups_section(parser)
    __reports_section(parser)
    __mapping_section(parser, issues)
    __storage_section(parser)
    __interop_section(parser, issues)
    __further_initialization()

    for issue in issues:
        LOG.exception(issue)


__all__ = "load_config"

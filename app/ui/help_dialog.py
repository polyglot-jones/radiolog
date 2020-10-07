import logging

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QHeaderView

LOG = logging.getLogger("main")



HELP_FONT = QFont("Segoe UI", 9)
HELP_FONT_STRIKEOUT = QFont("Segoe UI", 9)
HELP_FONT_STRIKEOUT.setStrikeOut(True)

(GuiSpec, GuiBaseClass) = uic.loadUiType("app/ui/help.ui")

class HelpDialog(GuiBaseClass, GuiSpec):
    def __init__(self, parent= None):
        GuiBaseClass.__init__(self)
        self.setupUi(self)
        self.parent=parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags((self.windowFlags() | Qt.WindowStaysOnTopHint) & ~Qt.WindowMinMaxButtonsHint & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())

    def stylize(self, statusStyleDict):
        self.hotkeys_table_widget.setColumnWidth(1, 10)
        self.hotkeys_table_widget.setColumnWidth(0, 145)
        # note QHeaderView.setResizeMode is deprecated in 5.4, replaced with
        # .setSectionResizeMode but also has both global and column-index forms
        self.hotkeys_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.hotkeys_table_widget.resizeRowsToContents()

        self.colorLabel1.setStyleSheet(statusStyleDict["At IC"])
        self.colorLabel2.setStyleSheet(statusStyleDict["In Transit"])
        self.colorLabel3.setStyleSheet(statusStyleDict["Working"])
        self.colorLabel4.setStyleSheet(statusStyleDict["Waiting for Transport"])
        self.colorLabel5.setStyleSheet(statusStyleDict["TIMED_OUT_ORANGE"])
        self.colorLabel6.setStyleSheet(statusStyleDict["TIMED_OUT_RED"])

        self.fsSomeFilteredLabel.setFont(HELP_FONT)
        self.fsAllFilteredLabel.setFont(HELP_FONT_STRIKEOUT)
        self.fsSomeFilteredLabel.setStyleSheet(statusStyleDict["Working"])
        self.fsAllFilteredLabel.setStyleSheet(statusStyleDict["Working"])

    def update_blinking(self, blinkToggle, statusStyleDict):

        if blinkToggle == 1:
            self.colorLabel4.setStyleSheet(statusStyleDict[""])
            self.colorLabel5.setStyleSheet(statusStyleDict["TIMED_OUT_ORANGE"])
            self.colorLabel6.setStyleSheet(statusStyleDict["TIMED_OUT_RED"])
            self.colorLabel7.setStyleSheet(statusStyleDict[""])
            self.fsSomeFilteredLabel.setFont(HELP_FONT_STRIKEOUT)
        else:
            self.colorLabel4.setStyleSheet(statusStyleDict["Waiting for Transport"])
            self.colorLabel5.setStyleSheet(statusStyleDict[""])
            self.colorLabel6.setStyleSheet(statusStyleDict[""])
            self.colorLabel7.setStyleSheet(statusStyleDict["STANDBY"])
            self.fsSomeFilteredLabel.setFont(HELP_FONT)

    def set_hotkeys(self):
        # FIXME Still need to actually place these hotkey description in the help window
        # FIXME These all currently only fetch the primary shortcut
        LOG.debug(f"help_info = {self.parent.action_help_info}")
        LOG.debug(f"options_dialog = {self.parent.action_options_dialog}")
        LOG.debug(f"print_dialog = {self.parent.action_print_dialog}")
        LOG.debug(f"open_log = {self.parent.action_open_log}")
        LOG.debug(f"reload_fleetsync = {self.parent.action_reload_fleetsync}")
        LOG.debug(f"restore_last_saved = {self.parent.action_restore_last_saved}")
        LOG.debug(f"mute_fleetsync = {self.parent.action_mute_fleetsync}")
        LOG.debug(f"filter_fleetsync = {self.parent.action_filter_fleetsync}")
        LOG.debug(f"toggle_team_hotkeys = {self.parent.action_toggle_team_hotkeys}")
        LOG.debug(f"increase_font = {self.parent.action_increase_font}")
        LOG.debug(f"decrease_font = {self.parent.action_decrease_font}")
        LOG.debug(f"to_team = {self.parent.action_to_team}")
        LOG.debug(f"to_teams_all = {self.parent.action_to_teams_all}")
        LOG.debug(f"from_team = {self.parent.action_from_team}")
        LOG.debug(f"from_team_1 = {self.parent.action_from_team_1}")
        LOG.debug(f"from_team_2 = {self.parent.action_from_team_2}")
        LOG.debug(f"from_team_3 = {self.parent.action_from_team_3}")
        LOG.debug(f"from_team_4 = {self.parent.action_from_team_4}")
        LOG.debug(f"from_team_5 = {self.parent.action_from_team_5}")
        LOG.debug(f"from_team_6 = {self.parent.action_from_team_6}")
        LOG.debug(f"from_team_7 = {self.parent.action_from_team_7}")
        LOG.debug(f"from_team_8 = {self.parent.action_from_team_8}")
        LOG.debug(f"from_team_9 = {self.parent.action_from_team_9}")
        LOG.debug(f"from_team_10 = {self.parent.action_from_team_10}")

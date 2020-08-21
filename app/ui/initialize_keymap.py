import os
import logging
from gwpycore import AppActions

LOG = logging.getLogger('main')

KEYMAP_FILENAME = "local/keymap.csv"
DEFAULT_KEYMAP = [
"Action Identifier,Action Label,Key Seq 1,Key Seq 2,Key Seq 3,Key Seq 4,Tip",
"helpInfo,Help Info,F1,,,,Display the help info box",
"optionsDialog,Options Dialog,F2,,,,Open the options dialog",
"printDialog,Print Dialog,F3,,,,Print reports",
"openLog,Open Log,F4,,,,Open a previous log",
"reloadFleetsync,Reload FleetSync,F5,,,,Reload the FleetSync table",
"restoreLastSaved,Restore Last Saved,F6,,,,Restore the last saved files",
"muteFleetsync,Mute FleetSync,F7,,,,Toggle muting FleetSync",
"toggleHotkeys,Toggle Legacy Hotkeys,F12,,,,Toggle legacy hotkeys",
"increaseFont,&Increase Font,=,,,,Increase the font size of the log text by 2 points.",
"decreaseFont,&Decrease Font,-,,,,Decrease the font size of the log text by 2 points.",
"toTeam,To a team,Right,t,,,New entry: To a team",
"toTeamsAll,To &all teams,a,,,,New entry: To all teams",
"fromTeam,From a team,Left,f,Enter,Space,New entry: From a team",
"fromTeam1,From team &1,1,,,,New entry: From team 1",
"fromTeam2,From team &2,2,,,,New entry: From team 2",
"fromTeam3,From team &3,3,,,,New entry: From team 3",
"fromTeam4,From team &4,4,,,,New entry: From team 4",
"fromTeam5,From team &5,5,,,,New entry: From team 5",
"fromTeam6,From team &6,6,,,,New entry: From team 6",
"fromTeam7,From team &7,7,,,,New entry: From team 7",
"fromTeam8,From team &8,8,,,,New entry: From team 8",
"fromTeam9,From team &9,9,,,,New entry: From team 9",
"fromTeam10,From team 1&0,0,,,,New entry: From team 10"
]

def initializeMainWindowActions(parent):
    parent.act = AppActions(parent)
    parent.act.loadKeyMapData(DEFAULT_KEYMAP, init_mode=True)
    if os.path.isfile(KEYMAP_FILENAME):
        LOG.info(f"Using shortcut key assignments per: {KEYMAP_FILENAME}")
        parent.act.loadKeyMapFile(KEYMAP_FILENAME)
    # parent.act.attachActions()
    parent.act.attachAction("increaseFont")
    parent.act.attachAction("decreaseFont")

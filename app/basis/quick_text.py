from app.logic.status_codes import StatusCode
from gwpycore import GlobalSettings
from pathlib import Path
import csv
import logging

LOG = logging.getLogger("main")

CONFIG = GlobalSettings("config")


def load_quick_text(dialog_id: str, asset_path: Path):
    """
    Reads the configured CSV file for the quick_text definitions for the given dialog.
    The file can be in the user's local folder, or in the assets/quick_text folder.
    If the configured file does not exist, then "assets/quick_text/default_texts.csv" will be used.
    The CSV file consist of 5 columns:
        0. The dialog ID (currently "entry", or "clue")
        1. The hotkey (F1 ~ F12)
        2. The text
        3. The associated icon (or blank)
    Any lines that do not begin with a valid dialog ID are merey skipped (comments, the header line, blank lines, whatever).

    Returns a list of tuples (all strings):
        (hotkey, text, icon).
    """
    text_list = []
    quick_text_path: Path = None
    if hasattr(CONFIG, "quick_text_path"):
        quick_text_path = CONFIG.quick_text_path
    if not quick_text_path or not quick_text_path.exists():
        quick_text_path = asset_path / "default_texts.csv"
    with quick_text_path.open("rt") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            if row:
                if row[0] == dialog_id:
                    (hotkey, text, icon) = (row[1], row[2], row[3])
                    text_list.append((hotkey, text, icon))
    return text_list


from configparser import ConfigParser
from pathlib import Path
from typing import List, Optional

def load_config(parent_path: str, config_path: Optional[str]) -> ConfigParser:
    config = ConfigParser()
    if config_path is None:
        script_dir = Path(parent_path)
        config_path = str(script_dir / "default.config")
    config.read(config_path)
    return config


def prettify_rows(rows: List[List[str]]) -> List[str]:
    column_widths = []
    for col_i in range(len(rows[0])):
        max_len = 0
        for row in rows:
            cell_length = len(row[col_i])
            if cell_length > max_len:
                max_len = cell_length
        column_widths.append(max_len)
    
    pretty_rows = []
    for row in rows:
        adjusted_cells = [cell.ljust(column_widths[i]) for (i, cell) in enumerate(row)]
        adjusted_row = "".join(adjusted_cells)
        pretty_rows.append(adjusted_row)
    return pretty_rows



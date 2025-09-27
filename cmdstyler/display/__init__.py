# modules
import os
import cmdstyler as cs
from textwrap import wrap

ts = os.get_terminal_size()

# global state
split_meta = {}
column_rows = {}  # track current row per section


def split(count: int = 1):
    """
    Draw vertical dividers across the terminal and store layout metadata.
    """
    global split_meta, column_rows, ts

    ts = os.get_terminal_size()
    cols = ts.columns
    rows = ts.lines

    sep_count = int(count)
    scount = sep_count + 1

    # separator positions
    sep_positions = []
    for j in range(1, sep_count + 1):
        pos = int(round(j * cols / scount)) - 1
        pos = max(0, min(cols - 1, pos))
        sep_positions.append(pos)

    # template line with separators
    base_line = [" "] * cols
    for p in sep_positions:
        base_line[p] = "|"
    base_line_str = "".join(base_line)

    # clear screen
    try:
        cs.cursor.clear("system")
    except Exception:
        print("\033[2J\033[H", end="")

    # draw full divider grid
    for _ in range(rows):
        print(base_line_str)

    # reset all column row counters to 1 (start from top)
    column_rows = {i: 1 for i in range(scount)}

    # save layout
    split_meta = {
        "count": sep_count,
        "scount": scount,
        "cols": cols,
        "sep_positions": sep_positions
    }


def printsplit(text: str, side: int = 0):
    """
    Print `text` into column `side` (0-based).
    Each column has its own row counter.
    """
    global split_meta, column_rows, ts

    if not split_meta:
        raise RuntimeError("split() must be called first")

    cols = split_meta["cols"]
    scount = split_meta["scount"]
    sep_count = split_meta["count"]

    side = max(0, min(scount - 1, int(side)))

    # calculate bounds for this column
    start_i = int(round(side * cols / scount))
    end_i = int(round((side + 1) * cols / scount))
    has_right_sep = (side < sep_count)
    content_width = end_i - start_i - (1 if has_right_sep else 0)
    if content_width < 1:
        content_width = max(1, end_i - start_i)

    # wrap text
    wrapped_lines = wrap(text, content_width)

    # start from that column's current row
    row = column_rows[side]

    for line in wrapped_lines:
        col_pos = start_i + 1  # 1-based
        cs.cursor.move(col_pos, row)

        to_print = line + " " * (content_width - len(line))
        print(to_print, end="")

        row += 1

    # update only this column’s row counter
    column_rows[side] = row

    # move cursor back to a safe place (doesn’t matter which)
    cs.cursor.move(1, max(column_rows.values()))
from openpyxl.utils import column_index_from_string
from enum import Enum

from openpyxl.styles import Font
from openpyxl.styles import borders
from openpyxl.utils import column_index_from_string
from copy import copy


def bold_cell(cell):
    f: Font = copy(cell.font)
    f.bold = True
    cell.font = f


def set_column_width(ws, col, width):
    ws.column_dimensions[col].width = width


class Side(Enum):
    LEFT = 1
    TOP = 2
    RIGHT = 3
    BOTTOM = 4


def add_thin_border(cell, side):
    o = copy(cell.border)
    s: borders.Side = borders.Side(border_style=borders.BORDER_THIN, color='000000')
    if side == Side.LEFT:
        o.left = s
    if side == Side.TOP:
        o.top = s
    if side == Side.RIGHT:
        o.right = s
    if side == Side.BOTTOM:
        o.bottom = s
    cell.border = o


def add_thin_border_to_row(ws, row_index, side):
    s: borders.Side = borders.Side(border_style=borders.BORDER_THIN, color='000000')
    b: borders.Border = None
    for row in ws.iter_rows(min_row=row_index, max_row=row_index):
        for cell in row:
            add_thin_border(cell, side)


def add_thin_border_to_column(ws, column_letter, side):
    s: borders.Side = borders.Side(border_style=borders.BORDER_THIN, color='000000')

    b: borders.Border = None
    idx = column_index_from_string(column_letter)

    for column in ws.iter_cols(idx):
        for cell in column:
            add_thin_border(cell, side)

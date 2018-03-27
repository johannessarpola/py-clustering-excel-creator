from typing import List

from openpyxl import Workbook
from openpyxl.worksheet import Worksheet

from app.src import excel_formatting_utils as formatting
from app.src.excel_formatting_utils import Side
from app.src import models


def extract_category_titles_from_cluster(cl):
    category_titles = set(cl.clusters[0].categories)
    return category_titles


class FormattingData(object):
    start_column = 0
    start_row = 0
    padding = 0

    def __init__(self, start_column,
                 start_row,
                 padding):
        self.start_column = start_column
        self.start_row = start_row
        self.padding = padding


def multiple_results_to_excels(base_fd: FormattingData, results, filename=None):
    """

    :param base_fd: FormattingData
    :param results: List of clustering results from multiple files
    :return:
    """
    wb = Workbook()
    ws = wb.create_sheet("Result", 0)
    col_cursor = base_fd.start_column
    for result in results:
        fd = FormattingData(col_cursor, base_fd.start_row, base_fd.padding)
        (cc, rc) = add_results_to_excel(fd, result, ws)
        col_cursor = cc  # This just increases to column by 4 for each iteration
    if filename is not None:
        return wb.save(f"{filename}")
    return wb.save(f"results.xlsx")



def add_results_to_excel(fd: FormattingData,
                         cls: List[models.InputClustering],
                         ws: Worksheet):
    """
    Appends results to workbook with current time as suffix
    :param fd:
    :param cls: list of models.InputClustering
    :param ws:
    :return:
    """

    category_titles = set()

    row_cursor = fd.start_row
    col_cursor = 0
    title_column = None
    category_columns = []
    for cl in cls:
        col_cursor = fd.start_column
        cluster_id = cl.id

        # get the category titles
        if len(category_titles) == 0:
            category_titles = extract_category_titles_from_cluster(cl)

        header_pass = True
        for cluster in cl.clusters:
            k = 0
            if header_pass:
                # Write cluster titlte
                title_cell = ws.cell(row=row_cursor, column=col_cursor, value=cluster_id)
                formatting.bold_cell(title_cell)
                if title_column is None:
                    title_column = title_cell.column
                ws.cell(row=(row_cursor + 1), column=col_cursor, value=cl.silhouette)
                col_cursor += 1
                # Write categories
                for cat_title in category_titles:
                    cat_cell = ws.cell(row=row_cursor, column=col_cursor + k, value=cat_title)
                    formatting.bold_cell(cat_cell)
                    if len(category_columns) <= len(category_titles):
                        category_columns.append(cat_cell.column)
                    k += 1
                formatting.add_thin_border_to_row(ws, row_cursor, Side.BOTTOM)
                row_cursor += 1

            k = 0
            # Write results per category
            for cat in category_titles:
                cat_count = cluster.categories[cat]
                ws.cell(row=row_cursor, column=col_cursor + k, value=cat_count)
                k += 1

            row_cursor += 1
            header_pass = False
        row_cursor += fd.padding
    col_cursor += len(category_titles)

    # Set some basic formatting
    formatting.set_column_width(ws, title_column, 20)
    formatting.add_thin_border_to_column(ws, title_column, Side.RIGHT)
    for c in category_columns:
        formatting.set_column_width(ws, c, 15)
        if c == c[-1:]:
            formatting.add_thin_border_to_column(ws, title_column, Side.RIGHT)
    return col_cursor, row_cursor

#!/usr/bin/env python3
"""
Module documentation
"""

import math
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function returns tuple containing start and end index
    hwich are pagination parameters for a page
    """
    if page > 0 and page_size > 0:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method uses the index_range function to return
        sepcified number of pages from file
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start > len(data):
            return [[]]
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        """
        rows = len(self.dataset())
        data = self.get_page(page, page_size)
        if self.get_page(page + 1, page_size) == [[]]:
            next_page = None
        else:
            next_page = page + 1
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(rows / page_size)
        _dict = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return _dict

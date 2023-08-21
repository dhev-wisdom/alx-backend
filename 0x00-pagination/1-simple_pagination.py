#!/usr/bin/python3
"""
Module documentation
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function returns tuple containing start and end index
    hwich are pagination parameters for a page
    """
    if page > 0 and page_size > 0:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size - 1

        return (start_index, end_index)

class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
    """Cached dataset
    """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

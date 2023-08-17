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

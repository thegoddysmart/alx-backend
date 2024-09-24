#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number
        page_size (int): The number of items per page.

    Returns:
        A tuple containing the start index and end index.
    """
    return ((page-1) * page_size, page_size * page)

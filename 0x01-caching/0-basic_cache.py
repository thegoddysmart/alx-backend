#!/usr/bin/env python3
"""
Basic Cache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements
    a caching system without any limit on the number of items.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Assigns the value item to the key in the cache
        If key or item is None, do nothing.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the key in the cache
        If key is None or doesn't exist, returns None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

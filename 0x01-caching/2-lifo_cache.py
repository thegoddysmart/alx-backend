#!/usr/bin/env python3
"""
LIFO Cache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements
    a caching system using LIFO algorithm for item eviction.
    """

    def __init__(self):
        """
        Initializes the LIFO cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the value item to the key in the cache.
        If key or item is None, do nothing.
        If the cache exceeds MAX_ITEMS,
        discard the last item put in cache.
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # Cache is full, discard the last item
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the key in the cache.
        If key is None or doesn't exist, returns None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

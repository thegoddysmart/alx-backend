#!/usr/bin/env python3
"""
MRU Caching module
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Add an item to the cache and discard the most recently used item
        if the cache exceeds MAX_ITEMS.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Get the item linked to key, if it exists, and mark it as most recently used
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None

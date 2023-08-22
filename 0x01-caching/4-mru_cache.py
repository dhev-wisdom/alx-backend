#!/usr/bin/python
"""
Basic Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Class inherits from BaseCaching
    Class is a caching system
    CLass uses the MRU Caching System
    MRU - Most Recently Used
    MRU discards the most recently used items first
    """
    def __init__(self):
        """
        Class constructor
        """
        super().__init__()
        self.keys = {}
        self.count = 0

    def put(self, key, item):
        """
        Assign value 'item' to key in self.cached_data
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
        you must discard the most recently used item (MRU algorithm)
        you must print DISCARD: with the key discarded and following by a new line

        """
        if key and item:
            self.cache_data[key] = item
            self.count += 1
            self.keys[key] = self.count
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            mru_hO = max(self.keys, key=lambda k: self.keys[k])
            del self.keys[mru_hO]
            mru = max(self.keys, key=lambda k: self.keys[k])
            del self.cache_data[mru]
            self.keys[mru_hO] = self.count
            del self.keys[mru]
            print(f'DISCARD: {mru}')

    def get(self, key):
        """
        return the value in cached_data dict linked to key
        """
        if key in self.cache_data:
            self.count += 1
            self.keys[key] = self.count
            return self.cache_data.get(key)
        return None

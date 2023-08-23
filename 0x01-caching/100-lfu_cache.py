#!/usr/bin/python
"""
Basic Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class inherits from BaseCaching
    Class is a caching system
    CLass uses the LFU Caching System
    LFU - Least Frequently Used
    LFU discards the least frequently used items first
    """
    def __init__(self):
        """
        Class constructor
        """
        super().__init__()
        self.keys = {}

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
        if key not in self.keys:
            self.keys[key] = 1
        else:
            self.keys[key] += 1
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            lfu = min(self.keys, key=lambda k: self.keys[k])
            del self.cache_data[lfu]
            del self.keys[lfu]
            print(f'DISCARD: {lfu}')

    def get(self, key):
        """
        return the value in cached_data dict linked to key
        """
        if key in self.cache_data:
            self.keys[key] += 1
            return self.cache_data.get(key)
        return None

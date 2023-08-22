#!/usr/bin/python
"""
Basic Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Class inherits from BaseCaching
    Class is a caching system
    """
    def __init__(self):
        """
        Class constructor
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign value 'item' to key in self.cached_data
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            last_key = self.keys.pop(-2)
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')

    def get(self, key):
        """
        return the value in cached_data dict linked to key
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None

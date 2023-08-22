#!/usr/bin/python
"""
Basic Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class inherits from BaseCaching
    Class is a caching system
    """
    def __init__(self):
        """
        Class constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign value 'item' to key in self.cached_data
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """
        return the value in cached_data dict linked to key
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None

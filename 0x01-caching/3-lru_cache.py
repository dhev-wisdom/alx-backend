#!/usr/bin/python
"""
Basic Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class inherits from BaseCaching
    Class is a caching system
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
        """
        if key and item:
            self.cache_data[key] = item
            self.count += 1
            self.keys[key] = self.count
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            lru = min(self.keys, key=lambda k: self.keys[k])
            # key_with_lowest_value = min(my_dict, key=lambda k: my_dict[k])
            del self.cache_data[lru]
            del self.keys[lru]
            print(f'DISCARD: {lru}')

    def get(self, key):
        """
        return the value in cached_data dict linked to key
        """
        if key in self.cache_data:
            self.count += 1
            self.keys[key] = self.count
            return self.cache_data.get(key)
        return None

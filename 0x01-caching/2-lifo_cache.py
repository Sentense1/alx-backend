#!/usr/bin/env python3
"""
Module for Lifo caching
"""
from base_caching import BaseCaching
from typing import Any, Optional, Dict


class LIFOCache(BaseCaching):
    """
    Last in first out Caching class
    """
    def __init__(self):
        """
        Initialize the class, and call the init of parent class
        """
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """
        Adds a key-value pair to cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                cache_data = list(self.cache_data.keys())
                last_key = cache_data[-1]
                self.cache_data.pop(last_key)
                print("DISCARD: {}".format(last_key))
                del last_key
        self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Dict]:
        """
        Retrieves a key from the cache
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()

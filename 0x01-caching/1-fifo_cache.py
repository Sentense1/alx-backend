#!/usr/bin/env python3
""" BaseCaching module
"""
from typing import Dict, Any, Optional
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Child class of BaseCaching, also stores data in dictionary
    """
    def __init__(self):
        """
        Calls the super of the parent class
        """
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """
        Put method for adding a data to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                cache_list = list(self.cache_data.keys())
                first_key = cache_list[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
                del first_key
            self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Any]:
        """
        Get method for retrieving the cache
        """
        if key is not None:
            return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = FIFOCache()
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

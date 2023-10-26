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
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """
        Adds a key-value pair to cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.rearrange_list(key)

    def get(self, key: Any) -> Optional[Dict]:
        """
        Retrieves a key from the cache
        """
        return self.cache_data.get(key)

    def rearrange_list(self, item: Any) -> None:
        """
        move an item to the last index of the self.queue list.
        """
        if self.queue[-1] != item:
            self.queue.remove(item)
            self.queue.append(item)


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

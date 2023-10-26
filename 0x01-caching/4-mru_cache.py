#!/usr/bin/env python3
""" MRU Caching """
from base_caching import BaseCaching
from typing import List, Any, Optional, Dict


class MRUCache(BaseCaching):
    """ MRU caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """ Puts item in cache """
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
            if self.queue[-1] != key:
                self.queue.remove(key)
                self.queue.append(key)

    def get(self, key: Any) -> Optional[Dict]:
        """ Gets item from cache """
        item = self.cache_data.get(key)
        if item is not None:
            if self.queue[-1] != key:
                self.queue.remove(key)
                self.queue.append(key)
        return item


if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()

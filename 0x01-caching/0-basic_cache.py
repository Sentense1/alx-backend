#!/usr/bin/python3
""" BaseCaching module
"""
from typing import Dict, Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Child class of BaseCaching, also stores data in dictionary
    """
    def __init__(self):
        """
        Calls the super of the parent class
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """
        Put method for adding a data to the cache
        """
        self.cache_data.get(key) = item

    def get(self, key: str) -> Optional[Any]:
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Elon")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))  # D returns None
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))

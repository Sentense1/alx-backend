#!/usr/bin/env python3
""" BaseCaching module
"""
from typing import Dict, Any


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self) -> None:
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item) -> None:
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")  # noqa

    def get(self, key) -> None:
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")  # noqa


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

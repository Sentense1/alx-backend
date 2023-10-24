#!/usr/bin/env python3
""" BaseCaching module
"""


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

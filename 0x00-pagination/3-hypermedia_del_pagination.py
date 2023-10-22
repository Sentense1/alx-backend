#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hyper method
        """
        # Ensure that page_size and index are valid integers
        assert isinstance(page_size, int) and page_size > 0
        assert index is None or (isinstance(index, int) and index >= 0)
        assert index < len(self.indexed_dataset())

        # Get the total number of rows in the dataset
        dataset_length = len(self.indexed_dataset())

        # Determine the current index (start index of the return page)
        current_index = 0 if index is None else index

        # Calculate the next index based on the page_size
        next_index = current_index + page_size

        # If there're deleted rows btwn d current & next index, adjust nxt_ind
        truncated_dataset = self.indexed_dataset()

        for i in range(current_index, next_index):
            if i >= len(truncated_dataset):
                break  # No more data to consider
            if truncated_dataset.get(i) is None:
                next_index += 1

        # Ensure that the current index is within a valid range
        #if current_index >= dataset_length:
        #    return {
        #            "index": 0,
        #            "next_index": None,
        #            "page_size": page_size,
        #            "data": []
        #    }

        # Ensure that the next index is within a valid range
        if next_index >= dataset_length:
            next_index = dataset_length

        # Retrieve the data for the current page
        indexed_data = self.indexed_dataset().values()
        data = list(indexed_data)[current_index:next_index]

        hyper_data = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return hyper_data


if __name__ == "__main__":
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")


    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first 
    #   data retreives is not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))

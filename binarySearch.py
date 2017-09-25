#!/usr/bin/env python3

import bisect

'''
The standard Python set() function is much faster than this binary search.
'''

class HashCollection(object):

    def __init__(self):
       self._sorted_hash_list = []
       self._nearest_index = 0

    def string_not_exists(self, to_check):
        hash_value = hash(to_check)
        try:
            nearest_index = bisect.bisect_left(self._sorted_hash_list, hash_value)
            return self._sorted_hash_list[nearest_index] != hash_value
        except(IndexError):
            return True

    def insert(self, new_string):
        hash_value = hash(new_string)
        bisect.insort_left(self._sorted_hash_list, hash_value)

if __name__ == "__main__":

    hash_collection = HashCollection()

    if hash_collection.string_not_exists('Essentials'):
        hash_collection.insert('Essentials')
    if hash_collection.string_not_exists('3ssentials'):
        hash_collection.insert('3ssentials')
    if hash_collection.string_not_exists('Essenti@ls'):
        hash_collection.insert('Essenti@ls')
    if hash_collection.string_not_exists('3ssentials'):
        hash_collection.insert('3ssentials')
    if hash_collection.string_not_exists('Essenti@ls'):
        hash_collection.insert('Essenti@ls')

    print(hash_collection._sorted_hash_list)

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:05:09 2020

@author: lveys
"""
from collections import OrderedDict
# Structures used:
# - dictionary for the cached items as it provides complexity O(1) for get / set / delete operations
# - OrderedDict() used to keep track of usage order. Used as a queue (least frequently used to most recently used key)

class LRU_Cache(object):

    # Initialize class variables
    def __init__(self, capacity):
        # Cache size
        self.capacity = capacity
        # Dictionary for cached items with get / insert / deletion complexity O(1)
        self.cache = OrderedDict()
        print('Cache set with maximum capacity of', self.capacity)


    # Retrieve item from provided key. Return -1 if nonexistent.
    def get(self, key):
        # check if key is a cache key
        if key in self.cache:
            # if key in cache, refresh usage ordering with move_to_end method (complexity O(1))
            self.cache.move_to_end(key)
            # return key associated value
            return self.cache[key]
        else:
            # if key not in cache returns -1
            return -1

    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
    def set(self, key, value):
        if self.capacity == 0:
            print('***Error*** The cache has a capacity of 0. Cannot add item.')
            return
        # if key not in cache, add to dictionary if capacity allows
        if key not in self.cache:
             # If cache at capacity, first remove the least recently used key as the first element of the orderedDict
            if len(self.cache) >= self.capacity:
                print('cache is full. Removing least recently used entry', self.cache.popitem(last = False))
            self.cache[key]=value
        # if key already in cache, refresh usage ordering with move_to_end method (alternative: pop/re-insert)
        else:
            print('element already in cache, refreshing the usage ordering')
            self.cache.move_to_end(key)
            


print('===================== Test case n°1 ========================')
our_cache = LRU_Cache(5)
print('cache initialization:')

print('additions to cache')
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print('cache status from least recently used to most recently used key = ', our_cache.cache)
print()

print('get key(1) -->', our_cache.get(1))       # returns 1
print('get key(2) -->', our_cache.get(2))       # returns 2
print('get key(9) -->', our_cache.get(9))      # returns -1 because 9 is not present in the cache

print('cache status from least recently used to most recently used key = ', our_cache.cache)
print()

print('===================== Test case n°2 ========================')
print('new addition to cache')
our_cache.set(5, 5)
print('new addition to cache')
our_cache.set(6, 6)

print('cache status from least recently used to most recently used key = ', our_cache.cache)
print()

print('===================== Test case n°3 ========================')
print('get key(3) -->', our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print('===================== Test case n°4 ========================')
print('new addition to cache')
our_cache.set(4, 4)
print('new addition to cache')
our_cache.set(7, 3)

print('cache status from least recently used to most recently used key = ', our_cache.cache)
print()

print('===================== Test case n°5 ========================')
print('get key(4) -->', our_cache.get(4))      # returns -1 because the key exists already in cache
print('get key(3) -->', our_cache.get(3))      # returns -1 because there is still no key = 3 in cache

print('cache status from least recently used to most recently used key = ', our_cache.cache)
print()

print('===================== Test case n°6 ========================')
our_cache = LRU_Cache(0)
print('cache initialization:')
print('cache status = ', our_cache.cache)
our_cache.set(1, 1)
print('get key(1) -->', our_cache.get(1))      # returns -1 because cache does not hold any item



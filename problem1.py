# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:05:09 2020

@author: lveys
"""

# Structures used:
# - dictionary for the cached items as it provides complexity O(1) for get / set / delete operations
# - list to keep track of usage order. Used as a queue (least frequently used to most recently used key)
#   the list is updated with append for entry and pop(0) for exit

class LRU_Cache(object):

    # Initialize class variables
    def __init__(self, capacity):
        # Cache size
        self.capacity = capacity
        # List to track key usage from least to last used element
        self.use_order = []
        # Dictionary for cached items with get / insert / deletion complexity O(1)
        self.cache = dict()


    # Retrieve item from provided key. Return -1 if nonexistent.
    def get(self, key):
        # check if key is a cache key
        if key in self.cache:
            # update usage tracking list by appending most recently used key (complexity O(1))
            self.use_order.append(key)
            # If usage tracking list is already at capacity then remove the least recently used key
            if len(self.use_order) > self.capacity:
                # remove least recently used with complexity O(1)
                self.use_order.pop(0)
            # return key associated value
            return self.cache[key]
        else:
            # if key not in cache returns -1
            return -1

    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
    def set(self, key, value):
        # if key in cache do nothing, else add to dictionary and update usage tracking list
        if key not in self.cache:
            self.cache[key]=value
            self.use_order.append(key)
            # If usage tracking list already at capacity then remove the least recently used key
            if len(self.use_order) > self.capacity:
                # If cache at capacity, first remove the least recently used key - complexity O(1)
                if len(self.cache) > self.capacity:
                    self.cache.pop(self.use_order[0])
                self.use_order.pop(0)



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print('cache initialization:')
print('cache status = ', our_cache.cache)
print('from least recently used to most recently used key: ', our_cache.use_order)
print()

print('get key(1) -->', our_cache.get(1))       # returns 1
print('get key(2) -->', our_cache.get(2))       # returns 2
print('get key(9) -->', our_cache.get(9))      # returns -1 because 9 is not present in the cache

print('cache status = ', our_cache.cache)
print('from least recently used to most recently used key: ', our_cache.use_order)
print()

print('additions to cache')
our_cache.set(5, 5) 
our_cache.set(6, 6)

print('cache status = ', our_cache.cache)
print('from least recently used to most recently used key: ', our_cache.use_order)
print()

print('get key(3) -->', our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print('additions to cache')
our_cache.set(4, 4) 
our_cache.set(7, 3)

print('cache status = ', our_cache.cache)
print('from least recently used to most recently used key: ', our_cache.use_order)
print()

print('get key(4) -->', our_cache.get(4))      # returns -1 because the key exists already in cache
print('get key(3) -->', our_cache.get(3))      # returns -1 because there is still no key = 3 in cache

print('cache status = ', our_cache.cache)
print('from least recently used to most recently used key: ', our_cache.use_order)
print()
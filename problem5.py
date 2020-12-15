# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:20:49 2020

@author: lveys
"""

import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
      
    def calc_hash(self):
      sha = hashlib.sha256()
      # define a hashable string to produce a unique hash key.
      # I chose data + timestamp because likely unique
      string = self.data + str(self.timestamp)
      hash_str = string.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
  
class Blockchain:
    def __init__(self):
        self.head = None
    
    def append(self, transaction):
        ''' add a new functional block to the blockchain
            input: transaction (str)
            output: updated blockchain with additional block transaction added to linked list
            Complexity O(n) with n = size of blockchain since we need to traverse the list
            '''
        # if blockchain not empty, add new transaction to the list
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            previous_hash = current.hash
            new_block = Block(datetime.now(), transaction, previous_hash)
            current.next = new_block
        # if blockchain empty, add new transaction as head of the list
        else:
            self.head = Block(datetime.now(), transaction, 0)
            
            
    def get_transaction(self, transaction):  # worst case complexity O(n) with n = size of blockchain
        '''find a transaction in the blockchain
            - input: a transaction (str)
            - returns the transaction details if found or -1 if transaction not found
            '''
        if transaction == None or type(transaction)!= str or self.head == None:
            return None
        
        item = self.head
        while item:
            if item.data == transaction:
                return (transaction, item.timestamp, item.hash)
            item = item.next
        return -1
    
    def get_hash(self, key):  # worst case complexity O(n) with n = size of blockchain
        '''find transaction corresponding to hash key in blockchain 
            - input: a hash key (str)
            - returns transaction details if found or -1 if transaction not found
            '''
        if key == None or type(key)!= str or self.head == None:
            return None
        
        item = self.head
        while item:
            if item.hash == key:
                return (item.data, item.timestamp, item.hash)
            item = item.next
        return -1
    
    def __repr__(self):  # complexity O(n) with n = size of blockchain
        '''helper function to print a blockchain with all transactions'''
        if self.head:
            current = self.head
            index = 1
            print('=============== start of blockchain ===================')
            while current:
                print('---------------- transaction n°', index,'---------------------')
                print(current.data)
                print('timestamp:', current.timestamp)
                print('hash key:', current.hash)
                index+=1
                current=current.next
            return '================== end of blockchain ==================='
        else:
            print('Blockchain is empty')



transaction_list = ['contract A', 'contract B', 'contract C', 'contract D']

blockchain = Blockchain()

for transaction in transaction_list:
    blockchain.append(transaction)

print('---------------------------------------')
print('find a specific transaction:')
output = blockchain.get_transaction('contract B')
for item in output:
    print(item)
print()
print('---------------------------------------')
print('find a specific hash key:')
output = blockchain.get_hash('d30d994cc1e839ada75b4527b2febd66764bd43388166abad52e28b9c3404f7a')
if output!=-1:
    print('the transaction corresponding to the hash key is: ')
    for item in output:
        print(item)
else:
    print('*** the hash key is not in the blockchain ***')
print()
print(blockchain)
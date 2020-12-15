# Show-me-the-data-structures
Solve six programing tasks usign advanced data structures (linked list, queues, recursive functions...)

These programming challenges are part of the scond project of UDACITY's [Data Structures & Algorithms Nanodegree Program]().

The questions cover a variety of topics related to the data structures learned in this course.The objective is to write up a clean and efficient solution in Python, taking into consideration the efficiency of the code and design choices. The code should be well explained, elegant and easy to read.

# Content

- Problem 1: Least Recently Used Cache
I use a dictionary for the cached items as it provides complexity O(1) for get / set / delete operations.
I also use a list to keep track of usage order. Used as a queue (least frequently used to most recently used key)
The list is updated with append for entry and pop(0) for exit therefore behaving as a queue structure.

- Problem 2: Finding Files
I use a search function with recursive approach using 'collect_files()' sub-function.
Because there is no real order to the elements, the complexity of the search is O(n): We must go through each element, n the number of items to explore

- Problem 3: Huffman coding, Data Compression
I use a list managed a a priority queue with append, pop and insert methods.
I use node and tree architecture. I use a recursive approach to traverse the tree and determine each code for each character. Each step has complexity O(n) in the worst case excepted building the Huffman tree which is O(nlogn). Therefore, overall time complexity is O(nlogn) in the worst case with n the number of characters to encode.
I observe compression of up to circa 2:1 in the tested examples.

- Problem 4: Active Directory
I use a Group class and a recursive search function 'is_user_in_group()'. The function checks if there is a sub-group and users attached in a recursive manner.
Worst case complexity is O(n), proportional to the number of elements within the group (and subgroups) since we must go through all users independently of the directory structure and how the users are allocated within this structure.

- Problem 5: Blockchain
I use a Blockchain class with severale methods: append, get_transaction, get_hash, and __repr__. The blockchain is built as a linked list of Blocks (Block class).
A block contains the timestamp of the transaction (when recorded), the data (content), the unique hash key (formed using timestamp and data which ensures a unique hash key) and a link to the hash of the previous transaction. An alternative is to use the previous hash + timestamp.
Complexity is O(n) with n = size of blockchain since we need to traverse the list in the worst case for all operations.

- Problem 6: Union and Intersection of Two Linked Lists
The Union and Intersection do not show duplicates. The output order is not important.
I used a linked list structure.
Union operation is of complexity O(n) with n the number of elements in the largest list. I approximate O(n1) + O(n2) to O(n) with n1 and n2 the number of items in each list.
Intersection operation has a complexity of O(n1*n2) so O(n^2) in worst case.

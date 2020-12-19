# Show-me-the-data-structures
Solve six programing tasks usign advanced data structures (linked list, queues, recursive functions...)

These programming challenges are part of the second project of UDACITY's [Data Structures & Algorithms Nanodegree Program](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256).

The questions cover a variety of topics related to the data structures learned in this course. The objective is to write up a clean and efficient solution in Python, taking into consideration the efficiency of the code and design choices. The code should be well explained, elegant and easy to read.

# Content

- Problem 1: Least Recently Used Cache
  - **Design choice**:
I use a dictionary for the cached items as it provides complexity O(1) for get / set / delete operations. More precisely, I use an orderedDict() structure to keep track of usage order. orderedDict() can be used as a queue to manage least frequently used to most recently used key. The dict() is updated with each operation therefore behaving as a queue structure.

  - **Time complexity**:
All operations have constant time.

  - **Space complexity**:
The max capacity is managed looking at the length of the dictionary.
Space complexity is O(capacity) which is equivalent to O(1) as it is independent from the number of operations performed.


- Problem 2: Finding Files
  - **Design choice**:
I use a search function with recursive approach using 'collect_files()' sub-function.

  - **Time complexity**:
Because there is no real order to the elements, the complexity of the search is O(n): We must go through each element, n the number of items to explore

  - **Space complexity**:
complexity is O(k) since we collect a  sub-list corresponding to the targeted suffix if k files have this suffix (with k <= n if there are n file paths in total). Generalizing, the worst case is O(n) if we have only one suffix. The best case would be O(1) if n is very large.


- Problem 3: Huffman coding, Data Compression
  - **Design choice**:
I use a list managed a a priority queue with append, pop and insert methods.
I use node and tree architecture. I use a recursive approach to traverse the tree and determine each code for each character. I observe compression of up to circa 2:1 in the tested examples.

  - **Time complexity**:
In the worst case each step has complexity O(n) excepted building the Huffman tree which is O(n^2) because we must traverse the sorted frequency list (size n) and then for each item, insert in the tree at the appriate place with worst case O(n) when we must compare against all frequencies. Therefore, overall time complexity is O(n^2) in the worst case with n the number of characters to encode.

  - **Space complexity**:
for an input data with n characters, I use:
    - a sorted list of size proportional to n in worst case (all characters are different)
    - another list used as a priority queue of same size as the sorted list => O(n) as well
    - This queue is transformed into the Huffman tree also proportional to n (several attributes per node with additional support internal nodes)
    - An encoded string and a dictionary char2code are generated, both of size O(n) in worst case
    - finally the decoded string of same size as the input, ie O(n)
Overall, the space complexity is a multiple of O(n) and is therefore O(n).


- Problem 4: Active Directory
  - **Design choice**:
I use a Group class and a recursive search function 'is_user_in_group()'. The function checks if there is a sub-group and users attached in a recursive manner.

  - **Time complexity**:
Worst case complexity is O(n), proportional to the number of elements within the group (and subgroups) since we must go through all users independently of the directory structure and how the users are allocated within this structure.

  - **Space complexity**:
Space complexity is of the order of the number of users plus the number of groups. We can assume the number of users will significanly exceed the groups and therefore the complexity of the structure is O(n).
The space complexity of our search operation is O(1) as we only return True/False if the user exists.


- Problem 5: Blockchain
**Design choice**
I use a Blockchain class with severale methods: append, get_transaction, get_hash, and __repr__. The blockchain is built as a linked list of Blocks (Block class).
A block contains the timestamp of the transaction (when recorded), the data (content), the unique hash key (formed using timestamp and data which ensures a unique hash key) and a link to the hash of the previous transaction. An alternative is to use the previous hash + timestamp.
**Time complexity**
Complexity is O(n) with n = size of blockchain since we need to traverse the list in the worst case for all operations.
**Space complexity**
Complexity is proportional to n (number of blocks in blockchain) since each block hase a number of attributes. So space complexity is O(n).


- Problem 6: Union and Intersection of Two Linked Lists
**Design choice**
The Union and Intersection do not show duplicates. The output order is not important.
I used a linked list structure and sets during intersection to avoid duplicate elements.
**Time complexity**
Union operation is of complexity O(n) with n the number of elements in the largest list. I approximate O(n1) + O(n2) to O(n) with n1 and n2 the number of items in each list.
Intersection operation has a complexity proportional to O(n1) + O(n2) with n1 and n2 the number of items in each list. Using sets, time complexity of searching set is O(1) on average. So Intersection operation is of complexity O(n) with n the number of elements in the largest list.
**Space complexity**
Union is O(n1+n2) so O(n). For intersection, I use a total of three sets with worst case 3 x O(n). The output intersection linkedlist is also worst case O(n). So in total, intersation is proportional to n and has worst case space complexity of O(n).

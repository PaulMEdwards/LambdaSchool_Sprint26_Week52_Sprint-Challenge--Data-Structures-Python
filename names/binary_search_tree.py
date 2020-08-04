"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

cur_dir = 'binary_search_tree'
import sys, pathlib
c = pathlib.Path.cwd()
# if str(c).endswith(cur_dir):
#     sys.path.insert(0, str(c.parent))
if str(sys.path[0]).endswith(cur_dir):
    sys.path.insert(0, str(c.parent))
# sys.path.insert(1, str(c.parent / 'queue'))

# print(sys.path)

try: from singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass
try: from singly_linked_list.singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass

# try: from queue import Queue
# except ModuleNotFoundError: pass
# except ImportError: pass
# try: from queue.queue import Queue
# except ModuleNotFoundError: pass
# except ImportError: pass

# from singly_linked_list.singly_linked_list import LinkedList
# import Queue

class Queue:
    def __init__(self):
        self.storage = LinkedList()
    def __len__(self):
        s = self.storage.length
        return s
    def enqueue(self, value):
        self.storage.add_to_tail(value)
    def dequeue(self):
        if self.storage.length == 0: return None
        v = self.storage.head.get_value()
        self.storage.remove_head()
        return v

class Stack:
    def __init__(self):
        self.storage = LinkedList()
    def __len__(self):
        return self.storage.length
    def push(self, value):
        self.storage.add_to_tail(value)
    def pop(self):
        if self.storage.length == 0: return None
        return self.storage.remove_tail()

DEPTH = [10]

def printUtil(node, gap):
    if (node is None):
        return
    gap += DEPTH[0]
    printUtil(node.right, gap)
    print()
    for i in range(DEPTH[0], gap):
        print(end = " ")
    print(f"{node.value} ({node.count})")
    printUtil(node.left, gap)
    print()

def printValues(node, label = None):
    if label: print(label)
    printUtil(node, 0)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1
        self.q = Queue()
        self.s = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            self.count += 1
            # print(f"incremented count for value:\t{self.value} ({self.count})")
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # printValues(self, f"inserted:\t{value}")

    # used in contains & delete
    def find(self, target):
        result = False
        n = self
        while result != True and n is not None:
            if target == n.value: result = True
            elif target > n.value:
                if n.right is not None:
                    n = n.right
                else:
                    n = None
            elif target < n.value:
                if n.left is not None:
                    n = n.left
                else:
                    n = None
            else:
                n = None
        # printValues(self, f"find {target}?\t{result}")
        return n

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target_value to cur_value
            # 1. == return True
            # 2. < go left
            # 3. > go right
            # 4. not found, return False
        result = False
        n = self.find(target)
        if n is not None: result = True
        # printValues(self, f"contains {target}?\t{result}")
        return result

    # Return the maximum value found in the tree
    def get_max(self):
        # print("get_max")
        n = self
        while n is not None:
            max = n.value
            n = n.right
        # print(f"max = {max}")
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        n = self
        # print(f"v: {n.value}\nl: {n.left}\nr: {n.right}\n")
        fn(n.value)
        if n.left is not None: n.left.for_each(fn)
        if n.right is not None: n.right.for_each(fn)

    # STRETCH
    def delete(self, value):
        # 1. not found
        # 2. root
        # 3. leaf (no children)
        # 4. left child only
        # 5. right child only
        # 6. left & right children
        n = self.find(target)
        # printValues(self, f"delete found target {target}?\t{result}")
        if n is not None:
            # TODO
            result = True
        else: result = False
        return result

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        n = self
        if n is not None:
            if n.left is not None:
                n.left.in_order_print()
            print(n.value)
            if n.right is not None:
                n.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        n = self
        while n is not None:
            if n.left is not None: self.q.enqueue(n.left)
            if n.right is not None: self.q.enqueue(n.right)
            print(n.value)
            n = self.q.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # Left, Root, Right
        n = self
        # self.s.push(n)
        # print(f"len: {len(self.s)}")
        # while len(self.s) > 0:
        #     n = self.s.pop()
        #     if n.right is not None: self.s.push(n.right)
        #     print(n.value)
        #     if n.left is not None: self.s.push(n.left)
        #     print(f"len: {len(self.s)}")
        stack = []
        stack.append(n)
        while len(stack) > 0:
            n = stack.pop()
            print(n.value)
            if n.right is not None: stack.append(n.right)
            if n.left is not None: stack.append(n.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # self.bft_print()
        # TODO
        pass

    def in_order_dft(self):
        self.in_order_print()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # self.dft_print()
        # TODO
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# printValues(bst, "values")

# print("in_order_print")
# bst.in_order_print()
# print("bft_print")
# bst.bft_print()
# print("dft_print")
# bst.dft_print()

# print("elegant methods")
# # print("pre order")
# # bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# # print("post order")
# # bst.post_order_dft()

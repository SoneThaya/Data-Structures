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

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if the value < Node's value
        if value < self.value:
            # we need to go left
            # if no left child,
            if self.left is None:
            # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
            # call the left child's insert method
                self.left.insert(value)
        # other wise, value >= Node's value
        else:
            # we need to go right
            # if we see there is no right child, 
            if self.right is None:
            # value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
            # call the right child's insert method
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checks the current node first
        if self.value == target:
            return True
        # if target is greater go right of node
        if target > self.value:
            #checks if right of node is None
            # target not found if None
            if self.right is None:
                return False
            # if there is a right run contains() again
            # it will check if current node equals target
            else:
                return self.right.contains(target)
        # if target is less than go left of current node
        if target < self.value:
            # checks if left of current node is None
            # if left is null target not found returns False
            if self.left is None:
                return False
            # if there is a left node runs contains() again
            # first step in contains() checks current node  to be target
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # right side of binary tree contains highest number
        # checks if right is None
        # if None returns current node as max
        if self.right is None:
            return self.value
        # if there is a right, call get_max() again until right is None
        else:
            return self.right.get_max()

    # DFS - Depth First Search
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # arr = []
        # cb = lambda x: arr.append(x)
        # fn is a call back function in the test file
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)
            
    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack= []
        stack.append(self)
        
        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()
            
            # add the current node's right child first
            if current.right:
                stack.append(current.right)
                
            # add the current node's left child
            if current.left:
                stack.append(current.left)
                
            # call the anonymous function
            fn(current.value)
            
    from collections import deque
    
    def iterative_breadth_first_for_each(self, fn):
        # BFT: FIFO
        # we'll use a queue to facilitate the ordering
        queue = deque()
        queue.append(self)
        
        # continue to traverse so long as there 
        while len(queue) > 0:
            current = queue.popleft()
            
            if current.left:
                queue.append(current.left)
                
            if current.right:
                queue.append(current.right)
            
            fn(current.value)
        
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if node is None:
        #     return
        
        # self.in_order_print(node.left)
        
        # print(node.value)
        
        # self.in_order_print(node.right)
        
        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        
        if self.right is not None:
            self.right.in_order_print(node)
        
        
        # current = node
        # stack = [] # initialize stack 
        # done = 0 
        
        # while True: 
        #     # Reach the left most Node of the current Node 
        #     if current is not None: 
        #         # Place pointer to a tree node on the stack  
        #         # before traversing the node's left subtree 
        #         stack.append(current) 
        #         current = current.left  
        #     # BackTrack from the empty subtree and visit the Node 
        #     # at the top of the stack; however, if the stack is  
        #     # empty you are done 
        #     elif(stack): 
        #         current = stack.pop() 
        #         print(current.value) 
        #         # We have visited the node and its left  
        #         # subtree. Now, it's right subtree's turn 
        #         current = current.right  
        #     else: 
        #         break
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        
        queue = Queue()
        
        queue.enqueue(node)
        
        while len(queue) > 0:
            node = queue.dequeue()
            print(node.value)
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        # use a queue
        # start with queue root node
        
        # while loop checks size of queue
        # size of queue
            # pointer variable
            # that updates at the
            #beginning of each loop

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        stack = Stack()
        
        stack.push(node)
        
        while len(stack) > 0:
            node = stack.pop()
            
            print(node.value)
            
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        # stack = []
        # stack.append(self)
        # # use a stack
        # # start your stack with the root node
        
        # # while loop that checks stack size
        #     # pointer
        # while len(stack) > 0:
        #     current = stack.pop()
        #     print(current)
            
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

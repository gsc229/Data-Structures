from dll_queue import Queue
from dll_stack import Stack
import sys
sys.path.append('../../queue_and_stack')
print(f"SYS.PATH: {sys.path}")


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        # left and right will each be an instance of BianarySearchTree with left and right instances of BianarySearchTree each with a left and right with instances and so on...
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is lsess than current node:
        if value < self.value:
            # is there already a value at self.left
            # no ->
            if not self.left:
                self.left = BinarySearchTree(value)
                # after the above line, left now IS A NEW 'self' with a it's own left and right and all the methods of the class!
            # yes ->
            else:
                self.left.insert(value)
        # if the value is greater:
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # go right
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

            # Return the maximum value found in the tree

    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            if node.left:
                self.in_order_print(node.left)
            print(f"{node.value}")
            if node.right:
                self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """
        DFT Steps:
        initialize a stack
        push root to stack
        while stack not empty
        pop top item out of stack into temp
        DO THE THING!!!!!!
        if temp has right right put into stack
        if temp has left left put into stack

        BFT Steps:
        initialize a queue
        push root to queue
        while stack not empty
        pop top item out of queue into temp
        DO THE THING!!!!!!
        if temp has right right put into queue
        if temp has left left put into queue

    """

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        temp = queue.storage.head.value
        while queue.size > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.right:
                queue.enqueue(temp.right)
            if temp.left:
                queue.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        temp = stack.storage.head.value
        while stack.size > 0:
            #print(f"STACK SIZE: {stack.size}")
            #print(f"TEMP: {temp.value}")
            print(temp.value)
            if temp.right:
                stack.push(temp.right)
            if temp.left:
                stack.push(temp.left)
            temp = stack.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        if node:
            print(f"{node.value}")
            if node.left:
                self.pre_order_dft(node.left)
            if node.right:
                self.pre_order_dft(node.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if node:
            if node.left:
                self.post_order_dft(node.left)
            if node.right:
                self.post_order_dft(node.right)
            print(f"{node.value}")


""" 
old code:

 """

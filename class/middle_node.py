class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


class Singly:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = Node(value)
        else:
            # we know the list has values
            self.head.insert_before(value)
            self.head = self.head.prev

    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = Node(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        # Planning if LL is empty
        # if node is either head or tail or both
        # if node is in middle
        if not self.head and not self.tail:
            print("ERROR: Attemped to delete node not in list")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    def mid(self):
        it_one = self.head
        it_two = self.head
        while it_two is not None:
            it_one = it_one.next
            it_two = it_two.next
            it_two = it_two.next
        print(it_one.value)
        return it_one.value

    def reverse(self):
        pass


""" 

iterate to the last node 

1n2 2n3 3n4 


 """

one = Node(1)
two = Node(2)
one.add(two)


""" 
class Node:
def __init__(self, value):
    self.value = value
    self.next = None
def add(self, value):
    self.next = Node(value)


 """

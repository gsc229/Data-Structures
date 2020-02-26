from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

import sys
sys.path.append('../doubly_linked_list')

# one = ListNode(1, None, 2)
# print(f"One {one.value}")

# two = ListNode(2, 1, 3)
# print(f"Two {two.value}")

# three = ListNode(3, 2, 5)
# print(f"Three {three.value}")

a = ListNode('a', None, None)
a.insert_after('b')
a.insert_after('c')
print(a.next.next.value)

from lru_cache import LRUCache
from lru_cache import DoublyLinkedList as Dll

cache = LRUCache(3)

cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
# cache.set('item2', 'z')
# cache.set('item4', 'z')

print(f"limit: {cache.limit}")
print(f"dictionary: {cache.storage}")
print(f"order: {cache.order}")

print("===========================")

DllA = Dll()
print(DllA.head)
DllA.add_to_head("HEAD")
DllA.add_to_head("NEW HEAD")
DllA.head.next.value = "OLD HEAD"
DllA.add_to_tail("TAIL")
DllA.add_to_tail("NEW TAIL")
print(f"\nhead.value: {DllA.head.value}\nhead.next.value: {DllA.head.next.value}\ntail.value: {DllA.tail.value}\nhead.next.next.next.value: {DllA.head.next.next.next.value}\nDllA length: {DllA.length}\nremoved head: {DllA.remove_from_head()}\nhead after remove: {DllA.head.value}\nremoved tail: {DllA.remove_from_tail()}\ntail after remove: {DllA.tail.value}")

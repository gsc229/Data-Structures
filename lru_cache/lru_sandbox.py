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

DllA.add_to_head("HEAD")

print(f"{DllA.head.value}")

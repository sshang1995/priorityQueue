from LinkedHeap import *

class PriorityQueue:

    def __init__(self):
        self.linked_heap = LinkedHeap()

    def add(self, key, value=None):
        self.linked_heap.insert(key, value)

    def remove(self):
        return self.linked_heap.delete()

    def min(self):
        return print(self.linked_heap.peek())

    def is_empty(self):
        return self.linked_heap.count == 0

    def __len__(self):
        return self.linked_heap.count


if __name__ == '__main__':
    pq = PriorityQueue()

    pq.add(11)
    pq.min()

    pq.add(7)
    pq.min()

    pq.add(8)
    pq.min()

    pq.add(6)
    pq.min()

    pq.add(5)
    pq.min()

    pq.add(9)
    pq.min()

    pq.add(4)
    pq.min()

    min_pair = pq.remove()
    print("delete first")
    print(min_pair)
    # print("current node:")
    # pq.min()

    min_pair = pq.remove()
    print("delete second")
    print(min_pair)
    # print("current node:")
    # pq.min()

    min_pair = pq.remove()
    print("delete third")
    print(min_pair)
    # print("current node:")
    # pq.min()



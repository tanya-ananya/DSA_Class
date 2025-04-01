import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        return None

    def extract(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def length(self):
        return len(self.heap)
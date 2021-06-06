"""
priority queue on python 
python has build in module for tis task :: heapq
"""
import heapq


class BasicPQ:
    #  O(n) time
    def __init__(self, ):
        self.queue = []

    def __str__(self):
        return " ".join([str(obj) for obj in self.queue])

    @property
    def is_empty(self):
        return len(self.queue) == 0

    def push(self, obj):
        self.queue.append(obj)

    @property
    def pop(self):
        if not self.is_empty:
            max = 0  # obj priority (in this case int value)
            for obj in self.queue:  # get max priority (bigest value)
                if max < obj:
                    max = obj
            self.queue.remove(max)
            return max
        else:
            print('queue is empty')
            exit(1)


if __name__ == "__main__":
    # q = BasicPQ()
    # q.push(2)
    # q.push(5)
    # q.push(1)
    # q.push(7)
    # q.push(10)

    # print(q)
    # while not q.is_empty:
    #     print(q.pop, end=" ")
    # print()

    li = [12, 6, 2, 56, 7, 3, 11]
    # print(f'before heapify : {li}')

    heapq.heapify(li)  # create binary heap
    print(f'created heap from : {li}')
    heapq.heappush(li, 4)
    print(f'after pushing : {li}')

    print(heapq.heappop(li))
    print(heapq.heappop(li))
    print(heapq.heappop(li))
    print(heapq.heappop(li))

    print(li)

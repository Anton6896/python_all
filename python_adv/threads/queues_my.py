import queue
import random
from random import Random

q = queue.LifoQueue()
num_list = random.sample(range(1, 50), 10)
for n in num_list:
    q.put(n)

if __name__ == "__main__":
    while not q.empty():
        print(q.get(), end=" ")
    print(" ")

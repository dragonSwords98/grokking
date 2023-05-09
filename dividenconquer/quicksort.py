# quicksort

from random import randrange
from typing import List
import numpy as np

def quicksort(n: List[int]) -> List:
    if len(n) <= 1:
        return n

    left = []
    right = []
    # pivot = n[0] # picking first element can create huge call stack if the array is already reasonably sorted
    # pivot = n[len(n)//2] # so instead, pick at least the middle, which is improvement, but no guarantee of average case all the time
    pivot = n[randrange(len(n) - 1)] # so pick a random pivot each time
    for i in range(1, len(n)):
        if n[i] > pivot:
            right.append(n[i])
        else:
            left.append(n[i])

    return quicksort(left) + [pivot] + quicksort(right)
    

for i in range(100):
    print(quicksort(np.random.randint(0, size=0)))
    print(quicksort(np.random.randint(1, size=1)))
    print(quicksort(np.random.randint(2, size=2)))
    print(quicksort(np.random.randint(2, size=10)))
    print(quicksort(np.random.randint(5, size=10)))
    print(quicksort(np.random.randint(15, size=10)))
    print(quicksort(np.random.randint(200, size=100)))
# GCF of area problem (euclid's algo, recursion)

def findGreatestCommonFactor(val1: int, val2: int) -> int:
    pass


def findLargestSquareBlocksInArea(length: int, width: int) -> int:
    smaller = min(length, width)
    if length <= 0 or width <= 0:
        return 0
    elif length % smaller == 0 and width % smaller == 0:
        return smaller
    else:
        return findLargestSquareBlocksInArea(smaller, max(length % smaller, width % smaller))


print(findLargestSquareBlocksInArea(0, 0))
print(findLargestSquareBlocksInArea(1, 1))
print(findLargestSquareBlocksInArea(1680, 640))
print(findLargestSquareBlocksInArea(16801, 24000))
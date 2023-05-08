def sum(nums: list[int]) -> int:
    if nums.length <= 0:
        return 0
    else:
        return nums[0] + sum(nums[1:])

def findMax(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    subMax = findMax(nums[1:])
    return nums[0] if nums[0] > subMax else subMax

# return index of a match in the arr
def binarySearch(arr: list, low: int, high: int, target: str) -> int:
    # recursive creates a call stack, occupying O(log n) space and time
    # iterative doesn't do this, occupying O(1) space and O(log n) time.

    pass
    # if len(arr) == 0:
    #     return None
    # if len(arr) == 1:
    #     return 0 if arr[0] else None
    # if arr[index] == target:
    #     return index
    # return binarySearch(arr, index/2)

# bonus: if i wanted to find the 'first match' using binary search
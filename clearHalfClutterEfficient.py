
# 1. identify what smallest set will remove half the integers in an array
# 2. first sort this array, so you know, then split it half. find out which 
# 3. 

# 2 <= arr.length <= 105
# arr.length is even.
# 1 <= arr[i] <= 105


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = dict()        
        target = len(arr)/2
        for a in arr:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
                
        o = sorted(counts.items(), key=lambda x: x[1])

        res = set()
        while target > 0 and len(o) > 0:
            item = o.pop()
            res.add(item[0])
            target -= item[1]

        return len(res)



s = Solution()
# result_set = s.minSetSize([3,3,3,3,5,5,5,2,2,7])
result_set = s.minSetSize([1,9])
print(result_set)
print(len(result_set))

# Contributed by: Bryan Ling
# original code from leetcode

from typing import List

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res=0
        l,r=0,len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        while l<r-1:
            if rightMax<leftMax:
                r-=1
                rightMax=max(height[r],rightMax)
                print('adding',rightMax-height[r],'to index', r)
                res+=rightMax-height[r]
            else:
                l+=1
                leftMax=max(height[l],leftMax)
                res+=leftMax-height[l]
                print('adding',leftMax-height[l],'to index', l)
        return res

# traverse the array from 0 to n

# find the min between the highest neighbor to my left and to my right
# - if i hit the edge and nothing is greater than me, exclude that side (or add zero)
# - when i find the max neighbor, that is where my pointer will go
# - when i find the min of the max neighbors, i add this to the sum

data = [
  [[5, 5, 5], [0]],
  [[1], [0]],
  [[0, 5], [0]],
  [[1, 0, 1], [1]],
  [[1, 0, 2], [1]],
  [[2, 0, 2], [2]],
  [[2, 0, 2, 0], [2]],
  [[2, 0, 2, 0, 2], [4]],
  [[2, 0, 2, 0, 2, 0], [4]],
  [[2, 0, 2, 0, 2, 0, 2], [6]],
  [[2, 0, 2, 0, 3, 0, 3], [7]],
  [[2, 0, 3, 0, 3, 0, 3], [8]],
  [[2, 0, 4, 0, 3, 0, 4], [11]],
  [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [6]],
  [[4, 2, 0, 3, 2, 5], [9]],
]

passes = []
fails = []
for idx, d in enumerate(data):
  s = Solution()
  value = s.trap(d[0])
  print('Test {}: should be {}, was {}'.format(idx, d[1][0], value))
  assert value == d[1][0]
  passes.append(idx)

print('All {} tests passed'.format(len(passes)))
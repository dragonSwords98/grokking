class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        res=0
        l,r=0,len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        print('left index', 'right index', 'left max', 'right max', 'res')
        while l<r-1:
            print(l, r, leftMax, rightMax, res)
            if rightMax<leftMax:
                r-=1
                rightMax=max(height[r],rightMax)
                res+=rightMax-height[r]
            else:
                l+=1
                leftMax=max(height[l],leftMax)
                res+=leftMax-height[l]
        return res
    

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])

# this is a O(n) operation that utilizes two runners, one from each side gradually coming to the middle
# the right runner's max encapsulates any water whenever it exceeds the left runner's max, so we count left runner's rain
# until it exceeds right runner's max, then we step the right runner until its max exceeds left runner, collecting rain along the way as (local max) - (current height of runner's pos)
# this will ensure O(n), 1 run through the entire list, while maintaining only single variables taking up O(n) space

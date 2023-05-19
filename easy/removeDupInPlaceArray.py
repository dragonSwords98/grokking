class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      # two runners
      run1 = 0
      # 2 runner runs to the end of the nums list finding the next unique value until end
      for run2 in range(len(nums)):
        if nums[run1] < nums[run2]:
          # 1 runner tracks the next index spot
          run1 += 1
          nums[run1] = nums[run2]

      return run1+1
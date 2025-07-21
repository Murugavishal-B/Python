from typing import List
# This is a brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
          return []
twosum = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
print(twosum) # Output: [0, 1]
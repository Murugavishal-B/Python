from typing import List
# This is a more efficient solution using a hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          hashmap={}
          for i in range(len(nums)):
            hashmap[nums[i]]=i
          for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i,hashmap[complement]]    
          return []
twosum = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
print(twosum) # Output: [0, 1]
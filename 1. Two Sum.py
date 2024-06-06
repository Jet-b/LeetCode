class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            remaining = target - nums[i] 
            if remaining in nums[0:i]:
                return [i, nums[0:i].index(remaining)]
            elif remaining in nums[i+1::]:
                return [i, nums[i+1::].index(remaining) + i + 1]


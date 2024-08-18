class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        leftBoundIndex = 0
        rightBoundIndex = len(nums) - 1
        
        while rightBoundIndex >= leftBoundIndex:
            mid = leftBoundIndex + (rightBoundIndex - leftBoundIndex)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rightBoundIndex = mid - 1
            else: # nums[mid] < target
                leftBoundIndex = mid + 1
        return leftBoundIndex

            
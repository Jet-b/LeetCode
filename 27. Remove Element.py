class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
            else:
                k += 1
        
        # bubble sort implementation to move the underscores to the end
        change = True
        while change:
            change = False
            for i in range(len(nums)-1):
                if nums[i] == "_" and nums[i+1] != "_":
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    change = True
        return k
        
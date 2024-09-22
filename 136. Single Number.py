class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        existing = set()
        unique_nums = set()
        for num in nums:
            if num not in existing:
                unique_nums.add(num)
                existing.add(num)
            elif num in existing:
                unique_nums.remove(num)
        for e in unique_nums:
            return e


# alternative solution using XOR however it only works for a list with only one unique number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
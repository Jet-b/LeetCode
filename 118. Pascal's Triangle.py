class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # two ways of doing it, through addition like this or factorial calculations
        nums = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(nums[i-1][j-1] + nums[i-1][j])
            nums.append(row)
        return nums
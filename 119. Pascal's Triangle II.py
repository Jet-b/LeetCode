class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [[1]]
        for i in range(1, rowIndex+1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(nums[i-1][j-1] + nums[i-1][j])
            nums.append(row)
        return nums[rowIndex]
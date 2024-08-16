
# sliding widnwo technique
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLength = len(needle)
        if needle == haystack:
            return 0
        for i in range(len(haystack)-needleLength+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
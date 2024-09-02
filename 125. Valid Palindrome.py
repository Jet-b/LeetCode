class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i.lower() for i in s if i.lower() in [j for j in "abcdefghijklmnopqrstuvwxyz0123456789"]]
        return s == s[::-1]
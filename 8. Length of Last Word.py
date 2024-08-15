# cheaty way
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])

# more complicated way

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        chars = False
        length = 0
        for i in range(len(s)):
            if s[i] == " " and chars:
                return length
            if chars:
                length += 1
            if s[i] != " " and not chars:
                chars = True
                length += 1
        return length
            
                
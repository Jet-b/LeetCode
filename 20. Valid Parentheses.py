class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracs = {"(":")","{":"}","[":"]"}
        stack = []
        for i in s:
            try:
                if i in bracs:
                    stack.append(i)
                elif bracs[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            except:
                return False
        if stack == []:
            return True
        else:
            return False



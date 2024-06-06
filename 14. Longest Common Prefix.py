class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = strs[0]
        for s in strs:
            if len(s) < len(shortest):
                shortest = s
        
        output = ""
        for i in range(len(shortest)):
            common = True
            for s in strs:
                if shortest[i] == s[i]:
                    continue
                else:
                    common = False
            if common:
                output+=shortest[i]
            else:
                return output
        return output



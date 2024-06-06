class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charlst = [char for char in s]
        longest = 0
        current = []
        for char in charlst:
            if char in current:
                if len(current) > longest:
                    longest = len(current)
                # check through the character before and add them if there are no repeats
                current.append(char)
                for i in range(len(current)):
                    if i+1 < len(current):
                        if current[i] in current[i+1:]:
                            current = current[i+1:]
            else:
                current.append(char)
        if len(current) > longest:
                    longest = len(current)
        return longest


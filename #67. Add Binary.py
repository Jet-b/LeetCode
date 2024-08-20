
# very bad solution

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = "0"
        ans = ""
        if len(a) < len(b):
            b, a = a, b
        for i in range(len(a)-len(b)):
            b = "0" + b
        for i in range(len(a)-1, -1, -1):
            if a[i] == "1" and b[i] == "1" and carry == "0":
                carry = "1"
                ans = "0" + ans
            if a[i] == "1" and b[i] == "1" and carry == "1":
                carry = "1"
                ans = "1" + ans
            if a[i] == "1" and b[i] == "0" and carry == "0":
                carry = "0"
                ans = "1" + ans
            if a[i] == "1" and b[i] == "0" and carry == "1":
                carry = "1"
                ans = "0" + ans
            if a[i] == "0" and b[i] == "1" and carry == "0":
                carry = "0"
                ans = "1" + ans
            if a[i] == "0" and b[i] == "1" and carry == "1":
                carry = "1"
                ans = "0" + ans
            if a[i] == "0" and b[i] == "0" and carry == "0":
                carry = "0"
                ans = "0" + ans
            if a[i] == "0" and b[i] == "0" and carry == "1":
                carry = "0"
                ans = "0" + ans
        return ans

# This code converts a Roman numeral string to an integer.
class Solution: 
    def romanToInt(self, s: str) -> int:
        m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(len(s)):
            if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
                num-=m[s[i]]
            else:
                num+=m[s[i]]
        return num
romantoint=Solution().romanToInt(s="MCMXCIV")
print(romantoint)  # Output: 1994
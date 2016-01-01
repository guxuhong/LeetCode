"""
 A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2. 
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        ans = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1]) not in (1, 2):
                    return 0
                else:
                    ans[1] = ans[0]
            elif int(s[i-1]) == 1 or (int(s[i-1]) == 2 and int(s[i]) < 7):
                ans[0], ans[1] = ans[1], ans[0] + ans[1]
            else:
                ans[0] = ans[1]
        return ans[1]

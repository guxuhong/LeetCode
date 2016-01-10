"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
 Given "25525511135", 
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.IpAddresses(ans, 1, '', s)
        return ans
    
    def IpAddresses(self, ans, num, temp, s):
        if num == 4:
            if s and (len(s) == 1 or (s[0] != '0' and int(s) <= 255)):
                ans.append(temp + s)
        else:
            for i in [1, 2, 3]:
                if s[:i] and int(s[:i]) <= 255:
                    self.IpAddresses(ans, num+1, temp+s[:i]+'.', s[i:])
                if s[:i] and s[0] == '0':
                    break

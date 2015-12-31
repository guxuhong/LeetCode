class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = 1
        for i in range(1, n):
            temp *= i
        ans = ''
        k -= 1
        nums = [i+1 for i in range(n)]
        while n > 0:
            cur = k / temp
            k %= temp
            ans += str(nums[cur])
            del nums[cur]
            n -= 1
            if n > 0: temp /= n
        return ans

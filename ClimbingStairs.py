class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 1
        b = 1
        tot = a+b
        for _ in range(n):
            a = b
            b = tot
            tot = a+b
        return a

from functools import cache;
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        waysToClimb = [0,1,2]
        if n==1:
            return 1
        if n==2:
            return 2
        if n>2:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
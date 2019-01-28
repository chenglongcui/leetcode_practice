class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cs = [1, 1, 2]
        if n >= 3:
            for i in range(3, n + 1):
                cs.append(cs[i-1]+cs[i-2])
        return cs[n]


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(4)
    print(result)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (right + left) // 2
            result = mid * mid
            if result > x:
                right = mid - 1
            elif result < x:
                left = mid + 1
            else:
                return mid
        return right
        # return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.mySqrt(10)
    print(result)

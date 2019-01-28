# 难点在与1.负数，2. 对于溢出的考虑
class Solution:
    def __init__(self):
        self.MAX_INT = 2 ** 31
        self.MIN_INT = -2 ** 31

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        temp = abs(x)
        # print(2 ** 31)
        while temp != 0:
            pop = temp % 10
            temp //= 10
            if result >= self.MAX_INT // 10:
                return self.MAX_INT
            elif result <= self.MIN_INT // 10:
                return self.MIN_INT
            result = result * 10 + pop
        if x < 0:
            return result * -1
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1463847412))

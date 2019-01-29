class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        for i in range(0, end // 2 + 1):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseString(
        ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"])
    print(result)

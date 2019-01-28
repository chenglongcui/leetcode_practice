class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dict_count = {}
        for num in nums:
            if num in dict_count:
                return True
            else:
                dict_count[num] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))

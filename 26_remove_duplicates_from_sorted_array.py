class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        for j in range(1, len(nums)):
            print(j)
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        print(i + 1, nums)
        return i + 1, nums


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1, 1, 2])

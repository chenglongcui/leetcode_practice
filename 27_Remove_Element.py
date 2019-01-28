class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print(i, nums)
        return i


if __name__ == '__main__':
    s = Solution()
    s.removeElement([3, 2, 2, 3], 2)

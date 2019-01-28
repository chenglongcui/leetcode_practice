class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_dict = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in idx_dict:
                result = [idx_dict[complement], i]
            else:
                idx_dict[nums[i]] = i
        print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    s.twoSum([15, 7, 11, 2], 9)

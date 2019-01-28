class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, n in enumerate(nums):
            print(n, i)
            if n in dict.keys() and i - dict[n]<=k:
                return True
            dict[n] = i
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        m -= 1
        n -= 1
        while (m >= 0) & (n >= 0):
            if nums1[m] >= nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1

            k -= 1

        while n >= 0:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1
        return nums1


if __name__ == '__main__':
    solution = Solution()
    result = solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
    print(result)

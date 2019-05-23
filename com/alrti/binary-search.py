# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2019/3/14
import unittest


class Solution:
    def searchInsert(self, nums, target) -> int:
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引
        :param nums:
        :param target:
        :return:
        """
        start, mid, end = 0, 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start

    def search(self, nums, target: int) -> int:
        """假设按照升序排序的数组在预先未知的某个点上进行了旋转,
        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1
        """
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[start] < nums[mid]:
                    if target >= nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
                elif nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif target > nums[mid]:
                if nums[start] < nums[mid]:
                    start = mid+1
                elif nums[start] > nums[mid]:
                    if nums[start] < target:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    end = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置
        :param nums:
        :param target:
        :return:
        """
        start, mid, end = 0, 0, len(nums)-1
        adr = [-1, -1]
        while start < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                if target > nums[mid-1] or mid==0:
                    adr[0] = mid
                elif target < nums[mid+1] or mid == len(nums)-1:
                    adr[1] = mid

        return adr

    def binary_search(self, nums, target, right=False):
        lo, hi = 0, len(nums)
        while lo < hi:
            # print("Trying to find %d at [%d, %d]" % (target, lo, hi))
            mid = (lo + hi) // 2
            # print("Comparing target %d with mid %d[#%d]" % (target, nums[mid], mid))
            if target > nums[mid] or (right and target == nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo


    # def searchRange(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     left = self.binary_search(nums, target)
    #     if left == len(nums) or nums[left] != target:
    #         return [-1, -1]
    #     right = self.binary_search(nums, target, True) - 1
    #     return [left, right]

    def countSmaller(self, nums):
        """
        给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量
        :param nums:
        :return:
        """
        dictnary = {}
        j = 0
        temp = nums.copy()
        lis = sorted(temp)
        for i in range(0, len(lis)):
            j += 1
            dictnary[str(lis[i])] = j

        counts = [0 for i in range(0, len(nums))]
        c = bitArray(len(nums))
        for i in range(len(nums) - 1, -1, -1):
            n = dictnary[str(nums[i])]
            counts[i] = c.get(n - 1)
            c.add(n, 1)

        return counts

    def mergekLists(self, lists):
        if not lists:
            return None
        res = []
        for a in lists:
            while a:
                res.append(a.val)
                a = a.next
        res.sort()
        p = ListNode(0)
        q = p
        for i in range(0, len(res)):
            q.next = ListNode(res[i])
            q = q.next
        return p.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class bitArray:
    def __init__(self, n):
        self.list = [0 for i in range(0, n+1)]
        self.n = n

    def add(self, x, num):
        while x < self.n:
            self.list[x] += num
            x += (x & (-x))

    def get(self, x):
        ans = 0
        while x > 0:
            ans += self.list[x]
            x -= (x & (-x))
        return ans


class TestBinarySearch(unittest.TestCase):
    def testSearch(self):
        target = 0
        nums = [4,5,6,7,0,1,2]
        result = Solution.searchRange(self, nums, target)
        print('%s :' + str(result))

    def testSearchRange(self):
        target = 0
        nums = [4,5,6,7,0,1,2]
        result = Solution.search(self, nums, target)
        print('%s :' + str(result))

    def testCountSmaller(self):
        nums = [5, 2, 6, 1]
        result = Solution.countSmaller(self, nums)
        print('%s :' + str(result))

    def testMerge(self):
        list = [[1, 4, 5], [1, 3, 4], [2, 6]]
        result= Solution.mergekLists(self, list)
        print('%s :' + str(result))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBinarySearch.testCountSmaller()))
    unittest.TextTestRunner().run(suite)





# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/9/19

import unittest


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums
        dp[0] = nums[0]
        max_val = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if max_val < dp[i]:
                max_val = dp[i]
        return max_val

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for i in range(amount)]
        dp[0] = 0
        for j in range(0, amount):
            for i in coins:
                if j - i >= 0 and dp[j-i] != -1:
                    if dp[j] == -1 or dp[j] > dp[j-i] + 1:
                        dp[j] = dp[j-i] + 1
        return dp[amount - 1]

    def minimumTotal(self, triangle):
        """
        :param triangle:List[List[int]]
        :rtype: int
        """
        if triangle == []:
            return 0
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(len(triangle[i]) - 1):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]


    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = [nums[0]]
        for i in range(1, len(nums)):
            if res[-1] < nums[i]:
                res.append(nums[i])
            else:
                pos = Solution.binarySearch(self, res, nums[i])
                res[pos] = nums[i]
        return len(res)

    def binarySearch(self, nums, target):
        start, end, mid = 0, len(nums)-1, 0
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        return start


    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 0

        dp = [([0] * len(dungeon[:][-1])) for i in range(len(dungeon))]
        num = dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(len(dungeon[-1][:]) - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1] - dungeon[-1][i])
        for j in range(len(dungeon) - 2, -1, -1):
            dp[j][-1] = max(1, dp[j+1][-1] - dungeon[j][-1])
        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[:][-1]) - 2, -1, -1):
                dp_min = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, dp_min - dungeon[i][j])

        return dp[0][0]


class Testcase(unittest.TestCase):
    def test(self):
        coins = [1, 2, 5, 7, 10]
        i = Solution.coinChange(self, coins, 14)
        print("the level is %s" % str(i))

    def testMiniTotal(self):
        nums = [[0,-3]]
        Solution.calculateMinimumHP(self, nums)


if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(unittest.makeSuite(Testcase.testMiniTotal()))
    unittest.TextTestRunner().run(test)



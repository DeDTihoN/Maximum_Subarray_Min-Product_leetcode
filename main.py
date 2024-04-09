from builtins import list
from typing import List


class Solution:
    MOD = 10 ** 9 + 7
    def getSumFromPref(self, prefSum, left, right):
        if left == 0:
            return prefSum[right]
        return prefSum[right] - prefSum[left - 1]
    def maxSumMinProduct(self, nums: List[int]) -> int:

        n = len(nums)
        leftMinBorder = [-1] * n
        rightMinBorder = [n] * n
        prefSum = [0] * n
        prefSum[0] = nums[0]

        for i in range(1, n):
            prefSum[i] = prefSum[i - 1] + nums[i]

        stack = [(0,nums[0])]
        for i in range(1, n):
            while stack and stack[-1][1] >= nums[i]:
                stack.pop()
            if stack:
                leftMinBorder[i] = stack[-1][0]
            else:
                leftMinBorder[i] = -1
            stack.append((i, nums[i]))

        stack = [(n - 1, nums[n - 1])]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] >= nums[i]:
                stack.pop()
            if stack:
                rightMinBorder[i] = stack[-1][0]
            else:
                rightMinBorder[i] = n
            stack.append((i, nums[i]))

        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * self.getSumFromPref(prefSum, leftMinBorder[i] + 1, rightMinBorder[i] - 1))

        return ans % self.MOD
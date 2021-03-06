"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List

class SolutionBrute:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, ele in enumerate(nums):
            for jdx, jle in enumerate(nums):
                if idx == jdx:
                    continue
                if (ele + jle) == target:
                    return [idx, jdx]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for idx, ele in enumerate(nums):
            diff = target - ele
            if (diff) in mem and mem[diff] != idx:
                return [mem[diff],idx]
            mem[ele] = idx

assert Solution().twoSum([3,3], 6) == [0,1]
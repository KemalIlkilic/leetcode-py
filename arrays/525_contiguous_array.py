"""
Problem: Contiguous Array
Difficulty: Medium
Problem Link: https://leetcode.com/problems/contiguous-array/description/
Time Complexity: O(n)
Space Complexity: O(n)

Description:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

from collections import defaultdict
from typing import List


def findMaxLength(self, nums: List[int]) -> int:
        sum_index = defaultdict(int)
        sum_index[0] = -1
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in sum_index:
                ans = max(ans,i-sum_index[prefix])
            else:
                sum_index[prefix] = i
        return ans
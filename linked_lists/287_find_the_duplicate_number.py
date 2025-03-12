"""
Problem: Find the Duplicate Number
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-the-duplicate-number/description/
Time Complexity: O(n)
Space Complexity: O(1)

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

Input: nums = [3,3,3,3,3]
Output: 3

"""

from typing import List
def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
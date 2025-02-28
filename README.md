# Leetcode Problem Solutions

This repository contains my solutions to various data structur

## Purpose

This repository serves as:

A personal archive of my problem-solving journey
A reference for common algorithmic patterns and techniques
A showcase of my coding skills and problem-solving approach

## Example Solution

"""
Problem: Two Sum
Difficulty: Easy
Problem Link: https://leetcode.com/problems/two-sum/
Time Complexity: O(n)
Space Complexity: O(n)

Description:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def twoSum(self, nums, target): # Create a hash map to store values and their indices
num_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach target
        complement = target - num

        # If complement exists in our map, we found our answer
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise, add current number to the map
        num_map[num] = i

    # No solution found (though the problem guarantees one exists)
    return []

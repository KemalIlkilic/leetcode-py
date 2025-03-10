"""
Problem: Happy Number
Difficulty: Easy
Problem Link: https://leetcode.com/problems/happy-number/description/
Time Complexity: O(n)
Space Complexity: O(1)

Description:
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

"""



def isHappy(self, n: int) -> bool:
        def square_sum(number):
            result = 0
            while number > 0:
                curr = number % 10
                result += (curr**2)
                number = number // 10
            return result

        slow = n
        fast = n
        while fast != 1 and square_sum(fast) != 1:
            slow = square_sum(slow) #1
            fast = square_sum(square_sum(fast)) #1
            if slow == fast:
                return False
        return True
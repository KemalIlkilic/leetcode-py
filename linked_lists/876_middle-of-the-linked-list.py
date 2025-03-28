"""
Problem: Middle of the Linked List
Difficulty: Easy
Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/
Time Complexity: O(n)
Space Complexity: O(1)


Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
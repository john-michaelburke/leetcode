"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val} {self.next}"
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return ListNode(l2.val, self.addTwoNumbers(None, l2.next))
        if l2 is None:
            return ListNode(l1.val, self.addTwoNumbers(l1.next, None))
        added_cur = l1.val + l2.val
        # print(added_cur, l1, l2)
        remainder = 0
        if added_cur > 9:
            remainder = 1
            added_cur %= 10
            if l1.next is None:
                l1.next = ListNode(remainder)
            else:
                l1.next.val += remainder
            
        return ListNode(added_cur, self.addTwoNumbers(l1.next, l2.next))

def ln_from_list(arr: List):
    l = None
    for ele in reversed(arr):
        l = ListNode(ele, l)
    return l

a = ln_from_list([3,4,2])
b = ln_from_list([4,6,5])
d = ln_from_list([7,0,8])
res = Solution().addTwoNumbers(a, b)
assert  res == d, f"{res} == {d}"
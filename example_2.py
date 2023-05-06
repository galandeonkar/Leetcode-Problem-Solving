'''
Given a linked list, return the node where the cycle begins. If there is no cycle,
return null.
Note: Do not modify the linked list.
Follow up: Can you solve it without using extra space?
URL: https://leetcode.com/problems/linked-list-cycle-ii/
'''

# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
def detectCycle(self, head):
"""
:type head: ListNode
:rtype: ListNode
"""
if head == None:
return head
else:
fast = head
slow = head
has_cycle = False
while fast != None and fast.next != None:
slow = slow.next
fast = fast.next.next
if fast == slow:
has_cycle = True
break
if has_cycle == False:
return None
slow = head
while fast != slow:
fast = fast.next
slow = slow.next
return slow


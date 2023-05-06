'''
Remove all elements from a linked list of integers that have value val.
Example Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6 Return: 1 --> 2 --> 3 -->
4 --> 5
URL: https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
def removeElements(self, head, val):
"""
:type head: ListNode
:type val: int
:rtype: ListNode
"""
if head == None:
return head
elif head != None and head.next == None:
if head.val == val:
return None
else:
return head
else:
dummy = ListNode(0)
dummy.next = head
prev = dummy
while head != None:
if head.val == val:
prev.next = head.next
head = prev
prev = head
head = head.next
return dummy.next

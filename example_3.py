'''
Given a singly linked list, determine if it is a palindrome.
Follow up: Could you do it in O(n) time and O(1) space?
URL: https://leetcode.com/problems/palindrome-linked-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
def isPalindrome(self, head):
"""
:type head: ListNode
:rtype: bool
"""
if head == None:
return True
elif head != None and head.next == None:
return True
else:
fast = head
slow = head
stack = []
while fast != None and fast.next != None:
stack.append(slow.val)
slow = slow.next
fast = fast.next.next
#madam
if fast != None:
slow = slow.next
while slow != None:
    if slow.val != stack.pop():
return False
else:
slow = slow.next
return True

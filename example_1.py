'''Write a program to find the node at which the intersection of two singly linked lists
begins.
For example, the following two linked lists:
A: a1 → a2 ↘ c1 → c2 → c3 ↗
B: b1 → b2 → b3 begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null. The linked lists must
retain their original structure after the function returns. You may assume there are
no cycles anywhere in the entire linked structure. Your code should preferably run
in O(n) time and use only O(1) memory.


URL: https://leetcode.com/problems/intersection-of-two-linked-lists/

'''

# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
"""
:type head1, head1: ListNode
:rtype: ListNode
"""
if headA == None and headB == None:
return None
elif headA == None and headB != None:
return None
elif headA != None and headB == None:
return None
else:
len_a = 0
len_b = 0
current = headA
while current != None:
current = current.next
len_a += 1
current = headB
while current != None:
current = current.next
len_b += 1
diff = 0
current = None
if len_a > len_b:
diff = len_a - len_b
currentA = headA
currentB = headB
else:
diff = len_b - len_a
currentA = headB
currentB = headA
count = 0
while count < diff:
currentA = currentA.next
count += 1
while currentA != None and currentB != None:
if currentA == currentB:
return currentA
else:
currentA = currentA.next
currentB = currentB.next

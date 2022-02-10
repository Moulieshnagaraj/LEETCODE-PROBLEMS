# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        firstptr = head
        secondptr = head

        while firstptr and firstptr.next:
            firstptr = firstptr.next.next
            secondptr = secondptr.next

        prev = None

        while secondptr:
            nxt = secondptr.next
            secondptr.next = prev
            prev = secondptr
            secondptr = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

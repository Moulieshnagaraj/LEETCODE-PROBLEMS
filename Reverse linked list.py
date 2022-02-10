class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        using dummynode or just using two pointers
        '''

        # dummy=ListNode()
        # current=head
        # while current:
        #     dummynxt = dummy.next
        #     currentnxt = current.next
        #     dummy.next=current
        #     current.next= dummynxt
        #     current=currentnxt
        # return dummy.next

        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
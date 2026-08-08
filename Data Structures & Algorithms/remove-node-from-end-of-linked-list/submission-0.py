# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        dummy=ListNode(0)
        dummy.next=head
        while head:
            l+=1
            head=head.next
        result=dummy
        j=0
        while dummy and dummy.next:
            if j==(l-n):
                dummy.next=dummy.next.next
                break
            j+=1
            dummy=dummy.next
        return result.next
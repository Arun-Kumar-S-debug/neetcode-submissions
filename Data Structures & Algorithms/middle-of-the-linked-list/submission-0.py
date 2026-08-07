# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len=0
        result=head
        while head:
            len+=1
            head=head.next
        j=1
        while j<=int(len/2):
            result=result.next
            j+=1
        return result
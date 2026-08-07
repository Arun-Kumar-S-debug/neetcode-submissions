# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result=None
        tail=None
        while head:
            if head.val==val:
                head=head.next
                continue
            temp=ListNode(head.val)
            if result==None:
                result=temp
                tail=temp
            else:
                tail.next=temp
                tail=tail.next
            head=head.next
        return result
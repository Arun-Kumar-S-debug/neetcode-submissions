# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        k=head
        head1=None
        while head:
            if head1==None:
                head1=ListNode()
                head1.val=head.val
                head=head.next
                continue
            temp=ListNode()
            temp.val=head.val
            temp.next=head1
            head1=temp
            head=head.next
        head=k
        while head and head1:
            if head.val==head1.val:
                head=head.next
                head1=head1.next
                continue
            return False
        return True
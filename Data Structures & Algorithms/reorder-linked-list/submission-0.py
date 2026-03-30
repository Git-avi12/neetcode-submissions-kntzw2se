# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #split list into 2
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l1=head
        l2=slow.next
        slow.next=None
        
        #reverse second list
        prev=None
        curr=l2
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l2=prev

        tail=l1
        while tail and l2:
            lt1=tail.next
            lt2=l2.next
            tail.next=l2
            l2.next=lt1
            tail=lt1
            l2=lt2
        print(l1)           
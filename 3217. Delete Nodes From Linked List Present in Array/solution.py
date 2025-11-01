# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        temp=head
        prev=None
        while(temp is not None):
            
            if(temp==head and temp.val in nums):
                head=head.next
            elif(temp.next==None and temp.val in nums):
                prev.next=None
            elif(temp.val in nums):
                prev.next=temp.next
                temp=prev
                
            prev=temp
            temp=temp.next

        return head

        

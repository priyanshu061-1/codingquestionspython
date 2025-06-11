
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=ListNode(0,head)
        dummy = temp

        for _ in range(n):
        
            head=head.next

        while head:
            head = head.next
            dummy=dummy.next
        dummy.next=dummy.next.next

        return temp.next



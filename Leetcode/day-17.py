#the trick fo this question is to stop before going to middle element and then remove the next varibale reffernce from it
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        if head.next is None:
            return 

        slow = head
        fast = head
        fast = fast.next.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next #here we delete the middle node
        return head
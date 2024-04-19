class Solution:
    def oddEvenList(self, head):
        if not head or not head.next : return head

        odd = head
        evenhead = even = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next
        odd.next = evenhead

        return head
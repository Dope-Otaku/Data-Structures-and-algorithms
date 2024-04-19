# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #reverse the first half of linked-list 
        slow, fast = head, head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        # first points to [n/2] - 1th node and moves left as we have reversed the first half
        first = reverse
        #second points to [n/2]th node and moves right as it has been left untouched 
        second = slow
        max_val = -math.inf
        while first :
            # checks for ith + (n-i-1)th node sum 
            if first.val + second.val > max_val:
                max_val = first.val + second.val
            first = first.next
            second = second.next
        return max_val
        
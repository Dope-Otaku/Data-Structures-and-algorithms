class Solution:
    def oddEvenList(self, head):
        
        if not head : return head                   # [1] trivial case
        
        dummy_odd = odd = ListNode(0, head)         # [2] initialize dummy nodes
        dummy_evn = evn = ListNode(0, head.next)    #     to facilitate iteration
                
        while odd.next and (odd := odd.next) and (evn := evn.next):
            
            if odd.next: odd.next = odd.next.next   # [3] skip one node for 
            if evn.next: evn.next = evn.next.next   #     both evens and odds
        
        odd.next = dummy_evn.next                   # [4] append evens to odds
        
        return dummy_odd.next
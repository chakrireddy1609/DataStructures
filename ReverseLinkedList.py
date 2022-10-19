class ReverseLL:

    def rev_ll(self,head):
        prev,curr = None,head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


rev = ReverseLL()

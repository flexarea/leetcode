# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast = slow = head
       # first find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        # None <- 1 -> 2 -> 3
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # iterate and swap
        last = prev
        first = head

        while last:
            next_first_node = first.next
            next_last_node = last.next

            # swap
            first.next = last
            last.next = next_first_node

            first = next_first_node
            last = next_last_node

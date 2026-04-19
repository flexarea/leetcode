# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n == 0:
            return head
        # reverse list
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # remove nth element

        counter = 1

        tmp = prev

        while tmp:
            if counter == n:
                if n == 1:
                    prev = tmp.next
                    tmp.next = None
                else:
                    tmp_prev.next = tmp.next
                break
            else:
                tmp_prev = tmp
                tmp = tmp.next
                counter += 1

        new_prev = None
        new_curr = prev

        while new_curr:
            next_node = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = next_node

        return new_prev

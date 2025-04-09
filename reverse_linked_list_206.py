# Reverse Linked List LeetCode #206
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr is not None:
            next_node = current.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


    def recursiveReverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is none or head.next is None:
            return head

        if head is None or head.next is None:
            return head

        new_head = self.recursiveReverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

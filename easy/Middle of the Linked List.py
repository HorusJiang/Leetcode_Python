class Solution:
    def middleNode(self, head):
        if head is None or head.next is None:
            return head
            
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast.next is not None:
            slow = slow.next            
        return slow
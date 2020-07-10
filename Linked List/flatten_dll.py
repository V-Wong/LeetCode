"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Flatten the list so that all the nodes appear in a single-level, doubly linked list
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flattenHelper(head: 'Node') -> 'Node':
            """
            Recursively flattens a list and returns the tail.
            """
            if not head:
                return None
            
            if head.child and not head.next:
                nestedHead, nestedTail = head.child, flattenHelper(head.child)
                head.next, nestedHead.prev = nestedHead, head
                head.child = None
            
            prev, cur = head, head.next
            while cur:
                if prev.child:
                    nestedHead, nestedTail = prev.child, flattenHelper(prev.child)
                    prev.next, nestedHead.prev = nestedHead, prev     
                    cur.prev, nestedTail.next = nestedTail, cur
                    prev.child = None
                    
                prev = cur
                cur = cur.next

            return prev
    
        if head:
            flattenHelper(head)
        return head
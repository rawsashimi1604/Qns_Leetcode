from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        currNode = head
        currVal = -150
        
        while currNode:
            # If currNode == currNode.val, skip the node and continue on.
            if currVal == currNode.val:
                prevNode.next = currNode.next
                
            # Else, make the currVal the currNode.val, then move prevNode to this node.
            else:
                currVal = currNode.val
                prevNode = currNode
            
            currNode = currNode.next
        
        return head
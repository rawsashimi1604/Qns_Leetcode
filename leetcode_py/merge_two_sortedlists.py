# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next}"

    def print_head(self):
        node = self.val
        nodes = []
        while node is not None:
            nodes.append(node)
            node = self.next
        nodes.append("None")
        print(nodes)
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         llist_head = ListNode(val=None)
#         selector = llist_head


head_n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(7)
n4 = ListNode(5)
n5 = ListNode(6)

head_n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(head_n1.print_head())
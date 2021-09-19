from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        outputArr = []
        if root == None:
            return outputArr

        current = root

        while (current != None or len(stack) != 0):
            while (current != None):
                stack.append(current)
                current = current.left

            current = stack.pop()
            outputArr.append(current.val)
            current = current.right

        return outputArr

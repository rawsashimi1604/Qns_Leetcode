from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0
        stack = []
        stack.append(root)

        while(len(stack) != 0):
            node = stack.pop()
            if(node.val >= low and node.val <= high):
                rangeSum += node.val

            if node.val > low and node.left != None:
                stack.append(node.left)
            if node.val < high and node.right != None:
                stack.append(node.right)

        return rangeSum

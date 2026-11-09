# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0
        v = self.step(root)
        return self.maxx
    def step(self, root: Optional[TreeNode]) -> int:
        #inorder 4 2 5 1 3
        if root == None:
            return 0
        a = self.step(root.left)
        b = self.step(root.right)         
        if (a+b)>self.maxx:
            self.maxx = a+b
        if a>=b:
            return 1+a
        elif b>a:
            return 1+b
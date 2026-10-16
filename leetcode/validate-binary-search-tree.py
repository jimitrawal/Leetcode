# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        mt = self.inorder(root, [])
        for i in range(len(mt)-1):
            if mt[i] >= mt[i+1]:
                return False
        return True
    def inorder(self, root, mt):
        if root == None:
            return mt 
        elif root.left and root.right:
            self.inorder(root.left, mt)
            mt.append(root.val)
            self.inorder(root.right, mt)
        elif root.left:
            self.inorder(root.left, mt)
            mt.append(root.val)
        elif root.right:
            mt.append(root.val)
            self.inorder(root.right, mt) 
        else:
            mt.append(root.val)
        return mt
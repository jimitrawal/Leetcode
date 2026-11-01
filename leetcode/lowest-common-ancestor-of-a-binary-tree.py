# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        listP = self.search(root, p, [])
        listQ = self.search(root, q, [])
        lowestCommon = root
        for i in range(min(len(listP),len(listQ))):
            if listP[i].val == listQ[i].val:
                lowestCommon = listP[i]
            else:
                break
        return lowestCommon
 
    def search(self, root: 'TreeNode', x: 'TreeNode', path) -> 'List':
        if root == None:
            return 
        elif root.val == x.val:
            path.append(root)
            return path
        else: 
            path.append(root)
            foundL = self.search(root.left, x, path)
            foundR = self.search(root.right, x, path)
            if foundL:
                return foundL
            elif foundR:
                return foundR
            else:
                path.pop()
                return
#problem: Valdiate binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
	def isValidBST(self,root:Optional[TreeNode])->bool:
		def valido(node,left,right):
			if node is None:
				return True
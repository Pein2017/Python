'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from binaryTree import TreeNode

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            ans = min(  ans, root.val , key = lambda x: abs( x - target )  )
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                return root.val
        return ans
2
if __name__ == '__main__' :
    print( "finished" )

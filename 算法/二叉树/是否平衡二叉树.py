'''
作者：卢沛安
时间：2022年09月25日
'''
from typing import List , Tuple , Dict , Optional
from binaryTree import TreeNode


def isBalanced( root: TreeNode ) -> bool :
    def height( root: TreeNode ) -> int :
        if not root :
            return 0
        leftHeight = height( root.left )
        rightHeight = height( root.right )
        if leftHeight == -1 or rightHeight == -1 or abs( leftHeight - rightHeight ) > 1 :
            return -1
        else :
            return max( leftHeight , rightHeight ) + 1

    return height( root ) != -1

    def height2( root: TreeNode ) -> int :
        if not root :
            return 0
        return max( height( root.left ) , height( root.right ) ) + 1

    if not root :
        return True
    return abs( height( root.left ) - height( root.right ) ) <= 1 and self.isBalanced( root.left ) and self.isBalanced(
        root.right )


if __name__ == '__main__' :
    print( "finished" )

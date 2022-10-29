'''
作者：卢沛安
时间：2022年10月29日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        def recur( A , B ):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur( A.left , B.left ) and recur( A.right , B.right )
        return recur( A , B ) or self.isSubStructure( A.left , B ) or self.isSubStructure( A.right , B )

if __name__ == '__main__' :
    print( "finished!" )

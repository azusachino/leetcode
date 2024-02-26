from typing import Optional
from local_tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p or q:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    p = None
    q = None
    r = s.isSameTree(p, q)
    print("isSameTree", r)

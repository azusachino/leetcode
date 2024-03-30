from typing import List, Optional
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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def maxDepth(node: Optional[TreeNode]) -> int:
            if node:
                l = maxDepth(node.left)
                r = maxDepth(node.right)
                self.max_depth = max(self.max_depth, l + r)
                return 1 + max(l, r)
            else:
                return 0

        maxDepth(root)

        return self.max_depth

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        r = None
        q = [root]
        while q:
            sz = len(q)
            for _ in range(sz):
                # pop(0) -> queue
                node = q.pop(0)
                r = node.val
                # traverse right, then left
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return r

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        odd = False
        while q:
            sz = len(q)
            pre = None
            for _ in range(sz):
                node = q.pop(0)
                if odd:
                    if node.val % 2 != 0:
                        return False
                    if pre and pre <= node.val:
                        return False
                else:
                    if node.val % 2 == 0:
                        return False
                    if pre and pre >= node.val:
                        return False
                pre = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            odd = not odd
        return True

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.buildTree(1, n)

    def buildTree(self, lo, hi):
        res = []
        if lo > hi:
            res.append(None)
            return res
        for i in range(lo, hi + 1):
            left = self.buildTree(lo, i - 1)
            right = self.buildTree(i + 1, hi)

            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


if __name__ == "__main__":
    s = Solution()
    p = None
    q = None
    r = s.isSameTree(p, q)
    print("isSameTree", r)

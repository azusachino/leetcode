from collections import defaultdict
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

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        pos = defaultdict(dict)

        # track all nodes' position
        def dfs(node, x, y):
            pos[x].setdefault(y, [])
            pos[x][y].append(node.val)
            if node.left:
                dfs(node.left, x - 1, y - 1)

            if node.right:
                dfs(node.right, x + 1, y - 1)

        dfs(root, 0, 0)

        """
        defaultdict(<class 'dict'>, {0: {0: [1], -2: [5, 6]}, -1: {-1: [2]}, -2: {-2: [4]}, 1: {-1: [3]}, 2: {-2: [7]}})
        """
        # print(pos)

        return [
            # sort vertical in reverse to simulate result order, sort(pos[x])
            ## in the same spot, smaller comes at first, sort(pos[x][y])
            [val for y in sorted(pos[x], reverse=True) for val in sorted(pos[x][y])]
            # return result from left to right, sort(pos)
            for x in sorted(pos)
        ]

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        alph = "abcdefghijklmnopqrstuvwxyz"
        self.res = [26]
        self.cur = []

        def dfs(node):
            self.cur.append(node.val)
            if not node.left and not node.right:
                self.res = min(self.res, self.cur[::-1])
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.cur.pop()

        dfs(root)

        return "".join(alph[i] for i in range(self.res))


if __name__ == "__main__":
    s = Solution()
    p = None
    q = None
    r = s.isSameTree(p, q)
    print("isSameTree", r)

from functools import cache
import sys
import turtle
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)


def deserialize(string):
    if string == "{}":
        return None
    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align="center", font=("Arial", 12, "normal"))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution:
    """
    95. Unique Binary Search Trees II
        https://leetcode.com/problems/unique-binary-search-trees-ii/description/
    96. Unique Binary Search Trees
        https://leetcode.com/problems/unique-binary-search-trees/description/
    98. Validate Binary Search Tree
        https://leetcode.com/problems/validate-binary-search-tree/description/
    99. Recover Binary Search Tree
        https://leetcode.com/problems/recover-binary-search-tree/description/
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def dfs(start, end):
            trees = []
            for i in range(start, end + 1):
                ls = dfs(start, i - 1)
                rs = dfs(i + 1, end)
                for l in ls:
                    for r in rs:
                        trees.append(TreeNode(i, l, r))
            return trees or [None]

        return dfs(1, n)

    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if not node:
                return True
            if l < node.val < r:
                return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
            return False

        return dfs(root, -sys.maxsize, sys.maxsize)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.x, self.y, self.prev = None, None, TreeNode(-sys.maxsize)

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            if not self.x and self.prev.val >= node.val:
                self.x = self.prev
            if self.x and self.prev.val >= node.val:
                self.y = node
            self.prev = node
            inorder(node.right)

        inorder(root)

        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val


class AnotherSolution:
    @cache
    def numTrees(self, n: int) -> int:
        """
        dp formula: numTrees(i-1) * numTrees(n-i)
        """
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        return res


if __name__ == "__main__":
    drawtree(deserialize("[1,2,3,null,null,4,null,null,5]"))
    drawtree(
        deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]")
    )

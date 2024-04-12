from typing import List, Optional

from tree.local_tree import TreeNode


class Solution:
    """
    1108. Defanging an IP Address
    1109. Corporate Flight Bookings
    1110. Delete Nodes And Return Forest
    1111. Maximum Nesting Depth of Two Valid Parentheses Strings
    """

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)

        for i, j, b in bookings:
            # at index i-1 (1-indexed), add n passengers
            res[i - 1] += b
            # at index j, remove n passengers
            res[j] -= b
        # at every index, how many passengers do we have
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # set for O(1) query
        to_delete = set(to_delete)
        self.res = []

        # only append root to result
        def dfs(node, is_root):
            if not node:
                return None
            # check whether current node is deleted
            deleted = node.val in to_delete
            # dfs left/right
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            if not deleted and is_root:
                self.res.append(node)
            return None if deleted else node

        dfs(root, True)
        return self.res

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/328841/java-c-python-o-1-extra-space-except-output/
        I had no idea.
        """
        return [i & 1 ^ (seq[i] == "(") for i, c in enumerate(seq)]

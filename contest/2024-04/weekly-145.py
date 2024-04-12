from typing import List, Optional

from tree.local_tree import TreeNode


class Solution:
    """
    1122. Relative Sort Array
    1123. Lowest Common Ancestor of Deepest Leaves
    1124. Longest Well-Performing Interval
    1125. Smallest Sufficient Team
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {v: i for i, v in enumerate(arr2)}
        # sort with custom lambda
        return sorted(arr1, key=lambda i: mp.get(i, 1000 + i))

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return depth, parent_node or itself (as the deepest single node)
        def dfs(node):
            if not node:
                return 0, None
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            # left subtree is deeper than right
            if ld > rd:
                return ld + 1, ln
            elif rd > ld:
                return rd + 1, rn
            else:
                # both left, right exsits, return their common ancestor
                return ld + 1, node

        return dfs(root)[1]

    def longestWPI(self, hours: List[int]) -> int:
        """
        We starts with a score = 0,
        If the working hour > 8, we plus 1 point.
        Otherwise we minus 1 point.
        We want find the maximum interval that have strict positive score.

        After one day of work, if we find the total score > 0,
        the whole interval has positive score,
        so we set res = i + 1.

        If the score is a new lowest score, we record the day by seen[cur] = i.
        seen[score] means the first time we see the score is seen[score]th day.

        We want a positive score, so we want to know the first occurrence of score - 1.
        score - x also works, but it comes later than score - 1.
        So the maximum interval is i - seen[score - 1]
        """
        ans = s = 0
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                # ans will be updated compare to s-1
                ans = i + 1
            elif s - 1 in pos:
                # backforth presum
                ans = max(ans, i - pos[s - 1])
            # save current presum
            if s not in pos:
                pos[s] = i
        return ans

    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        """
        NP problem, BruteForce DP
        https://leetcode.com/problems/smallest-sufficient-team/editorial/
        """
        n = len(people)
        m = len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(n):
                new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)
                    if (
                        dp[skills_mask] == -1
                        or people_mask.bit_count() < dp[skills_mask].bit_count()
                    ):
                        dp[skills_mask] = people_mask
            return dp[skills_mask]

        answer_mask = f((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans

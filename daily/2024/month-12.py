from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        12.01
        1346. Check If N and Its Double Exist
        https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01

        class Solution {
        public:
            bool checkIfExist(vector<int>& arr) {
                unordered_set<int> seen;
                for (int num : arr) {
                    if (seen.count(num * 2) || (num % 2 == 0 && seen.count(num / 2))) {
                        return true;
                    }
                    seen.insert(num);
                }
                return false;
            }
        };
        """
        pass

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        12.02
        1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
        https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2024-12-02
        class Solution {
        public:
            int isPrefixOfWord(string sentence, string searchWord) {
                // Split the sentence into words
                istringstream stream(sentence);
                string word;
                int index = 1; // 1-based index

                while (stream >> word) {
                    // Check if the word starts with the searchWord
                    if (word.find(searchWord) == 0) {
                        return index;
                    }
                    index++;
                }

                // Return -1 if no word starts with the searchWord
                return -1;
            }
        };
        """
        pass

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        12.03
        2109. Adding Spaces to a String
        https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03
        """
        ans = []
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(" ")
                j += 1
            ans.append(c)
        return "".join(ans)

    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        """
        12.04
        2825. Make String a Subsequence Using Cyclic Increments
        https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/?envType=daily-question&envId=2024-12-04
        """
        j, n, m = 0, len(s1), len(s2)
        for i in range(n):
            if j < m and (ord(s2[j]) - ord(s1[i])) % 26 <= 1:
                j += 1
        return j == m

    def canChange(self, start: str, target: str) -> bool:
        """
        12.05
        2337. Move Pieces to Obtain a String
        https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05
        """
        n = len(start)
        i = j = 0
        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1
            if n in (i, j):
                return i == j == n
            if start[i] != target[j]:
                return False
            if start[i] == "L":
                if i < j:
                    return False
            else:
                if i > j:
                    return False
            i += 1
            j += 1
        return True

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        12.06
        2554. Maximum Number of Integers to Choose From a Range I
        https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range/description/?envType=daily-question&envId=2024-12-06
        """
        st = set(banned)
        i = 1
        cur = 0
        res = 0
        while i <= n:
            if i in st:
                i += 1
                continue
            cur += i
            if cur > maxSum:
                return res
            res += 1
            i += 1
        return res

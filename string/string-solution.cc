#include <string>

using namespace std;

class Solution
{
public:
    // https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint
    string getSmallestString(string s, int k)
    {
        for (char &c : s)
        {
            int left = c - 'a';
            int right = 'z' - c + 1;
            int dis = min(left, right);
            if (dis <= k)
            {
                k -= dis;
                c = 'a';
            }
            else
            {
                k = 0;
                c -= dis;
            }
        }
        return s;
    }
};
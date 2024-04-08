#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    // https://leetcode.com/problems/powerful-integers/
    vector<int> powerfulIntegers(int x, int y, int bound)
    {
        unordered_set<int> s;
        for (int xp = 1; xp <= bound; xp *= x)
        {
            for (int yp = 1; xp + yp <= bound; yp *= y)
            {
                s.insert(xp + yp);
            }
        }
        return vector<int>(s.begin(), s.end());
    }
    // https://leetcode.com/problems/broken-calculator/
    int brokenCalc(int startValue, int target)
    {
        // think reversely, multiply+substract becomes divide+add
        int res = 0;
        // 1. y = y / 2
        // 2. y = y + 1
        while (target > startValue)
        {
            if (target % 2 == 1)
            {
                target++;
            }
            else
            {
                target /= 2;
            }
            res++;
        }
        // target <= startValue
        return res + (startValue - target);
    }
    // https://leetcode.com/problems/flower-planting-with-no-adjacent/
    // paint all gardens with {1,2,3,4}, and no adj has the same color
    vector<int> gardenNoAdj(int n, vector<vector<int>> &paths)
    {
        vector<vector<int>> adj(n);
        // graph to adj table
        for (vector<int> &p : paths)
        {
            adj[p[0] - 1].push_back(p[1] - 1);
            adj[p[1] - 1].push_back(p[0] - 1);
        }

        vector<int> res(n);
        for (int i = 0; i < n; ++i)
        {
            // colors fit {1,2,3,4} (use 5 to mitigate index conversion)
            int colors[5] = {};
            // mark already used color
            for (int j : adj[i])
            {
                colors[res[j]] = 1;
            }
            // find unused color
            for (int c = 4; i > 0; --i)
            {
                if (!colors[c])
                {
                    res[i] = c;
                }
            }
        }
        return res;
    }
};
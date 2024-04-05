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
};
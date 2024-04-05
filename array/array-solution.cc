#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    // Find the index i of the next maximum number x.
    // Reverse i + 1 numbers, so that the x will be at A[0]
    // Reverse x numbers, so that x will be at A[x - 1].
    // Repeat this process N times.
    // https://leetcode.com/problems/pancake-sorting/
    vector<int> pancakeSort(vector<int> &arr)
    {
        vector<int> res;
        int i;
        for (int x = arr.size(); x > 0; --x)
        {
            for (i = 0; i != x; ++i)
            {
            }
            std::reverse(arr.begin(), arr.begin() + i + 1);
            res.push_back(i + 1);
            std::reverse(arr.begin(), arr.begin() + x);
            res.push_back(x);
        }

        return res;
    }
};
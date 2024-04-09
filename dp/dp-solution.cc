#include <vector>

using namespace std;

class Solution
{
public:
    int maxSumAfterPartitioning(vector<int> &arr, int k)
    {
        int n = arr.size();
        vector<int> dp(n + 1);
        for (int i = 1; i <= n; ++i)
        {
            int cur_max = 0, best = 0;
            for (int j = 1; j <= k && i - j >= 0; ++j)
            {
                cur_max = std::max(cur_max, arr[i - j]);
                best = std::max(best, dp[i - j] + cur_max * j);
            }
            dp[i] = best;
        }
        return dp[n];
    }
};
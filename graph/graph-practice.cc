#include <vector>

using namespace std;

class MaximalRectangle
{
public:
    // try to find out all valid rectangles by brute force
    int maximalRectangle1(vector<vector<char>> &M)
    {
        if (!size(M))
            return 0;
        int ans = 0, m = size(M), n = size(M[0]);
        for (int start_i = 0; start_i < m; start_i++)
            for (int start_j = 0; start_j < n; start_j++)
                for (int end_i = start_i; end_i < m; end_i++)
                    for (int end_j = start_j; end_j < n; end_j++)
                    {
                        bool allOnes = true;
                        for (int i = start_i; i <= end_i && allOnes; i++)
                            for (int j = start_j; j <= end_j && allOnes; j++)
                                if (M[i][j] != '1')
                                    allOnes = false;
                        ans = max(ans, allOnes * (end_i - start_i + 1) * (end_j - start_j + 1));
                    }

        return ans;
    }
    // optimized brute force, by check '1' before-hand
    int maximalRectangle2(vector<vector<char>> &M)
    {
        int res = 0;
        int m = size(M), n = size(M[0]);
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                for (int row = i, colLen = n, col; row < m && M[row][j] == '1'; row++)
                {
                    for (col = j; col < n && M[row][col] == '1'; col++)
                    {
                    }
                    colLen = min(colLen, col - j);
                    res = max(res, (row - i + 1) * colLen);
                }
            }
        }
        return res;
    }
    // Pre-compute consecutive 1s to the right / DP
    int maximalRectangle(vector<vector<char>> &M){}
};
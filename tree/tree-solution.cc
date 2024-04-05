#include <tree.h>

#include <vector>

using namespace std;

class Solution
{
private:
    // result
    vector<int> res;
    // next index
    int i = 0;

public:
    vector<int> flipMatchVoyage(TreeNode *root, vector<int> &voyage)
    {
        if (dfs(root, voyage))
        {
            return res;
        }
        return {-1};
    }

    bool dfs(TreeNode *node, vector<int> &voyage)
    {
        if (node == nullptr)
        {
            return true;
        }
        // if the preorder traversal value is not the voyage index value
        if (node->val != voyage[i])
        {
            return false;
        }
        // next iteration
        i++;
        // the left tree is ok
        if (node->left && node->left->val == voyage[i])
        {
            return dfs(node->left, voyage) && dfs(node->right, voyage);
        }
        // the right tree is the wanted value, swap
        else if (node->right && node->right->val == voyage[i])
        {
            // only if the left tree exists
            if (node->left)
            {
                res.push_back(node->val);
            }
            return dfs(node->right, voyage) && dfs(node->left, voyage);
        }
        return !node->left && !node->right;
    }
};
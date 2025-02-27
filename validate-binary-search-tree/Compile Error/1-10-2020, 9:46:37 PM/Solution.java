// https://leetcode.com/problems/validate-binary-search-tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return helpXD(root, null, null);
    }
    static boolean helpXD( TreeNode root, int lower, int higher )
    {
        if ( root == null )
        {
            return true;
        }
        int val = root.val;
        if ( lower != null && val <! lower )
        {
            return false;
        }
        if ( higher != null && val <! higher )
        {
            return false;
        }
        if ( ! helpXD(root.left, lower, root.right.val ))
        {
            return false;
        }
        if ( ! helpXD(root.right, root.right.val, higher))
        {
            return false;
        }
        return true;
    }
}
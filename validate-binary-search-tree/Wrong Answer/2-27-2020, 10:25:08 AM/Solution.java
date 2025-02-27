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
        if ( root == null )
        {
            return true;
        }
        TreeNode t1 = root;
        TreeNode t2 = root;
        return helper(t1,t2);
    }
    public static boolean helper(TreeNode t1, TreeNode t2 )
    {
        if ( t1 == null && t2 == null )
        {
            return true;
        }
        if ( t1 == null || t2 == null )
        {
            return false;
        }
        return helper(t1.left,t2.right) && helper(t1.right, t2.left);
    }
}
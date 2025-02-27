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
        if (root.right != null )
        {
            if ( root.val >= root.right.val )
            {
                return false;
            }
        }
        if (root.left != null )
        {
            if ( root.val <= root.left.val )
            {
                return false;
            }
        }
        return isValidBST(root.left) && isValidBST(root.right);
    }
}
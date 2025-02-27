// https://leetcode.com/problems/symmetric-tree

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
    public boolean isSymmetric(TreeNode root) {
        return helpMe(root, root);
    }
    public boolean helpMe(TreeNode t1, TreeNode t2 )
    {
        if ( t1 == null && t2 == null ){return true;}
        if ( t1 == null || t2 == null ){return false;}
        return t1.val == t2.val && helpMe(t1.left, t2.right) && helpMe(t1.right, t2.left);
    }
}
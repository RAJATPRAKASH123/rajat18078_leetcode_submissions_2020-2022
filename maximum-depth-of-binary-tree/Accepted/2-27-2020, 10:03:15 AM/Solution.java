// https://leetcode.com/problems/maximum-depth-of-binary-tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.lang.Math;
class Solution {
    public int maxDepth(TreeNode root) {
        if ( root == null )
        {
            return 0;
        }
        return Math.max( 1 + maxDepth(root.left), 1 + maxDepth(root.right) );

    }
}
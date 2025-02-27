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
        return helpMe(root, null, null);
    }
    
    public boolean helpMe(TreeNode root, Integer lower, Integer upper )
    {
        if ( root ==  null )
        {
            return true;
        }
        if ( upper != null && root.val >= upper ){return false;}
        if ( lower != null && root.val <= lower ){return false;}
        
        int val = root.val;
        if ( !helpMe(root.left, lower, val)){return false;}
        if ( !helpMe(root.right, val, upper)){return false;}
        return true;
    }

}
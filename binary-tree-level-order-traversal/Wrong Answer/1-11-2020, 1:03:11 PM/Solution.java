// https://leetcode.com/problems/binary-tree-level-order-traversal

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lot = new ArrayList<List<Integer>>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        while ( !q.isEmpty() )
        {
            List<Integer> temp = new ArrayList<Integer>();
            List<TreeNode> temp3 = new ArrayList<TreeNode>();
            temp.add(root.val);
            temp3.add(root);
            while( !q.isEmpty())
            {
                TreeNode temp2 = q.remove();
                if( temp2.left != null )
                {
                    q.add(temp2.left);
                    temp3.add(temp2.left);
                    temp.add(temp2.left.val);
                }
                if ( temp2.right != null )
                {
                    q.add(temp2.right);
                    temp3.add(temp2.right);
                    temp.add(temp2.right.val);
                } 
            }
            lot.add(temp);
        }
        return lot;
    }
}
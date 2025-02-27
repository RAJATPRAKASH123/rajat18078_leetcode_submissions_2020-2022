// https://leetcode.com/problems/k-closest-points-to-origin

import java.util.*;
class Solution {

    public int[][] kClosest(int[][] points, int K) {
        Comparator<int[]> cmp = new Comparator<int[]>()
        {
            @Override
            public int compare(int[] a, int[] b){
                int x = a[0] * a[0] + a[1] * a[1];
                int y = b[0] * b[0] + b[1] * b[1];
                return x < y ? -1 : x == y ? 0 : 1;        
            }  
        };
        PriorityQueue<int[]> pq = new PriorityQueue<>(cmp);
        int[][] r = new int[K][];
        for ( int i = 0; i < points.length;++i){
            pq.offer(points[i]);
        }
        for ( int i = 0; i < K ;++i){
            r[i] = pq.poll();
        }
        return r;
    }
}
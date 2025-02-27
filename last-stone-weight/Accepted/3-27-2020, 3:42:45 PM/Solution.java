// https://leetcode.com/problems/last-stone-weight

import java.util.*;
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for ( int i = 0;  i < stones.length; i++ ){
        pq.offer(stones[i]);
        }
        while ( pq.size() > 1){
            int a = pq.poll();
            int b = pq.poll();
            if (Math.abs(a - b) == 0){
                continue;
            }else{
                pq.offer(Math.abs(a - b) );
            }
        }
        if ( pq.size() == 1) {
            return pq.poll();
        }
        return 0;
            
    }
}
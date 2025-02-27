// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution {
    public int maxProfit(int[] prices) {
        if ( prices.length == 0 && prices.length == 1 )
        {
            return 0;
        }
        int temp = -1234567;int count = 0;
        boolean flag = false;
        for ( int i = 1; i < prices.length; i++ )
        {
            if (prices[i] >= prices[i-1] )
            {
                if ( flag == false )
                {
                    temp = prices[i - 1];
                    flag = true;
                }
            }else if ( prices[i] < prices[i-1] )
            {
                if ( flag == true )
                {
                    flag = false;
                    count += prices[i-1] - temp;
                    temp = prices[i];
                }
            }
            if ( i == prices.length - 1 && temp != -1234567 && prices[i] > temp)
            {
                count += prices[i] - temp;
            }
            //System.out.println(count);
        }
        return count;
    }
}
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick

class Solution
{
    private:
        int minCost(int start,int end,const vector<int>& cuts,vector<vector<int>>& costs)
        {
            if(start==end-1)
                return 0;
            else if(costs[start][end]!=-1)
                return costs[start][end];
            
            int min_cost=INT_MAX;
            for(int i=start+1; i<end; ++i)
            {
                int cost = (cuts[end]-cuts[start]) +  minCost(start,i,cuts,costs) +  minCost(i,end,cuts,costs);
                min_cost=min(min_cost,cost);
            }
            costs[start][end]=min_cost;
            return min_cost;
        }
    public:
        int minCost(int n, vector<int>& cuts)
        {
            cuts.push_back(0);
            cuts.push_back(n);
            sort(cuts.begin(),cuts.end());
            int k=cuts.size();
            vector<vector<int>> costs(k,vector<int>(k,-1));
            minCost(0,cuts.size()-1,cuts,costs);
            return costs[0][k-1];
        }
};

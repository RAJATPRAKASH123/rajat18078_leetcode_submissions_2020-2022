// https://leetcode.com/problems/two-sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        vector< pair<int, int> > sorted;
        for ( int i = 0; i < length; ++i ){
            sorted.push_back({ nums[i], i});
        }
        
        sort( sorted.begin(), sorted.end());
        
        int left = 0;
        int right = length - 1;
        while (left < right){
            int sum = sorted[left].first + sorted[right].first;
            if (sum == target){
                return {sorted[left].second, sorted[right].second};
            }
            if (target < sum ){
                --right;
            }else{
                ++left;
            }
        }
        return {};
    }
};
/*
class Solution{
public:
	vector<int> twoSum(vector<int> &nums, int target)
	{
		int length = nums.size();

		vector<pair<int, int>> sorted;
		for (int i = 0; i < length; ++i)
			sorted.push_back({ nums[i], i });
		::sort(sorted.begin(), sorted.end());

		int left = 0;
		int right = length - 1;
		while (left < right)
		{
			int sum = sorted[left].first + sorted[right].first;
			if (sum == target)
				return { sorted[left].second, sorted[right].second };

			if (target < sum)
				--right;
			else
				++left;

		}
		return {};
	}
};
*/
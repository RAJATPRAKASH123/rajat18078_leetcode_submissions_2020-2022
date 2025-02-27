// https://leetcode.com/problems/find-in-mountain-array


class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int ans=-1;
        int start=0;
        int end= mountainArr.length()-1;
        long mid;
        while(start<end){
            mid= start+(end-start)/2;
            if(mountainArr.get(mid)<mountainArr.get(mid+1)){
                start= mid+1;
            }
            else{
                end= mid;
            }
        }
        int peak= start;
        if(target==mountainArr.get(peak)){
            return peak;
        }
        start=0; end=peak-1;
         
        while(start<=end){
            mid= start+(end-start)/2;
            if(target>mountainArr.get(mid)){
                start=mid+1;
            }
            else{
                end= mid-1;
            }
         
        }
        if(target==mountainArr.get(start)){
            return start;
        }
        start=peak;
        end=mountainArr.length()-1;
        while(start<=end){
            
            mid= start+(end-start)/2;
            // cout<<mid<<endl;
            if(target >= mountainArr.get(mid)){
                end= mid-1;
            }
            else{
               start=mid+1;
            }
           // cout<<start<<endl;
        }
         if(target==mountainArr.get(start)){
                return start;
            }
        
        
        
       return -1; 
    }
};
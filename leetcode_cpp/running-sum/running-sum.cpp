#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
public:
    vector<int> runningSum(vector<int>& nums) 
    {
        int sum = 0;
        vector<int> output(nums.size());
        for (int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];
            output[i] = sum;
        }
        return output;
    }
};

int main()
{
    Solution test;
    vector<int> obj = {1,1,1,1,1};
    vector<int> result = test.runningSum(obj);
    for (int i = 0; i < 5; i++)
    {
        cout << obj[i] << '\n';
    }
    return 0;
}
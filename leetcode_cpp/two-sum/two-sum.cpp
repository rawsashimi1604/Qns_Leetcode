#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
public:
    vector<int> twoSum(vector<int> &nums, int target) 
    {   
        vector<int> output(2);
        for (int i = 0; i < nums.size(); i++)
        {   
            for (int j = 0; j < nums.size(); j++)
            {
                if (j == i)
                {
                    continue;
                }
                if (nums[i] + nums[j] == target)
                {   
                    output[0] = i;
                    output[1] = j;
                    break;
                }
            }
        }

        cout << output[0] << '\n';
        cout << output[1] << '\n';
        return output;
    }
};

int main ()
{
    Solution test;
    vector<int> input = {2,7,11,15};
    vector<int> result = test.twoSum(input, 9);
    
    return 0;
}
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

class Solution 
{
public:
    vector<int> sortedSquares(vector<int>& nums) 
    {   
        vector<int> output(nums.size());
        for (int i = 0; i < nums.size(); i++)
        {
            output[i] = pow(nums[i], 2);
        }
        sort(output.begin(), output.end());
        return output;
    }
};

int main ()
{

    return 0;
}


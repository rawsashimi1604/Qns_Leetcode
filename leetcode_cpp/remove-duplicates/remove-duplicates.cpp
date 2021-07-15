#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
public:
    int removeDuplicates(vector<int>& nums) 
    {
        // Add a counter
        int counter = 0;

        // Iterate through the nums
        for (int i = 0; i < nums.size(); i++)
        {
            // If current element is equal next element skip this iteration.
            if (i < nums.size() - 1 && nums[i] == nums[i+1])
            {
                continue;
            }

            // Update the array in place.
            else
            {
                nums[counter] = nums[i];
                counter++;
            }
        }
        // Remove extra duplicates from vector
        nums.resize(nums.size() - (nums.size() - counter));
        return counter;
    }
};

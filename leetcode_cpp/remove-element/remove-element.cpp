#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution 
{
public:
    int removeElement(vector<int>& nums, int val) 
    {   
        int counter = 0; // Non duplicate counter
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == val)
            {
                continue;
            }
            else
            {
                nums[counter] = nums[i];
                counter++;
            }
        }
        // erased
        int erased = nums.size() - counter;

        for (int i = 0; i < nums.size(); i++)
        {
            cout << i << ' ' << nums[i] << '\n';
        }
        cout << "k = " << counter << '\n';
        return counter;
    }
};

int main ()
{
    Solution test;
    vector<int> testVec = {1, 1, 2, 3, 3, 4, 5, 5};
    int result = test.removeElement(testVec, 5);
    return 0;
}

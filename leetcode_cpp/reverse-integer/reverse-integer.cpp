#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <chrono>

using namespace std;

class Solution 
{
    public:
        int reverse(int x) 
        {
            int MINVAL = pow(-2, 31);
            int MAXVAL = pow(2, 31) - 1;

            // If x fits the constraints
            if (MINVAL <= x && x <= MAXVAL)
            {
                // Check if negative number
                bool negative = false;
                int num = x;
                if (x < 0)
                {   
                    negative = true;
                }

                // Reverse
                string strVal = to_string(num);
                string reverseVal = "";
                for (int i = strVal.length() - 1; i >=0; i--)
                {
                    reverseVal += strVal[i];
                }
                
                int reversedInt;
                try
                {
                    reversedInt = (negative) ? -stoi(reverseVal) : stoi(reverseVal);
            
                }
                catch (out_of_range)
                {
                    return 0;
                }
                if (MINVAL <= reversedInt && reversedInt <= MAXVAL)
                {
                    return reversedInt;
                }
                else
                {
                    return 0;
                }
            }
            else
            {
                return 0;
            }
        }
};

int main()
{   
    // Start measuring run time of code.
    auto begin = chrono::high_resolution_clock::now();

    Solution test;
    int testVal = test.reverse(-50010000);
    cout << testVal << '\n';

    // Stop measuring run time and calculate the elapsed time
    auto end = chrono::high_resolution_clock::now();
    auto elapsed = chrono::duration_cast<chrono::nanoseconds>(end - begin);

    printf("Time measured: %.3f seconds. \n", elapsed.count() * 1e-9);
    return 0;
}

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution 
{
    public:
        vector<int> plusOne(vector<int>& digits) 
        {
            if (1 <= digits.size() && digits.size() <= 100)
            {
                // Loop through elements in vector from last to first.
                // If digit is not 9, continue add 1 and break
                // Else if digit is 9  and index is not first, add 1
                // Else first digit become 0, add 1 at the start of vector

                for (int i = digits.size() -1; i >= 0; i--)
                {
                    if (digits[i] != 9)
                    {
                        digits[i] += 1;
                        break;
                    }

                    else if (digits[i] == 9 && i != 0)
                    {
                        digits[i] = 0;
                    }

                    else
                    {
                        digits[0] = 0;
                        digits.insert(digits.begin(), 1);
                    }
                }
                return digits;
            }
            else
            {
                return {};
            }
        }
};
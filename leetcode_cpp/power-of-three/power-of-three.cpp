#include <iostream>
#include <cmath>

using namespace std;

class Solution 
{
    public:
        bool isPowerOfThree(int n) 
        {
            if (pow(-2, 31) <= n && n <= pow(2, 31) -1)
            {
                if (n == 1)
                {
                    return true;
                }

                else if (n % 3 != 0 || n == 0)
                {
                    return false;
                }

                else 
                {
                    return isPowerOfThree(n/3);
                }
            }
            else
            {
                return false;
            }
        }
};

int main ()
{
    Solution test;
    bool result = test.isPowerOfThree(9);
    cout << result;
    return 0;
}
#include <iostream>
#include <cmath>

using namespace std;

class Solution 
{
public:
    bool isPowerOfTwo(int n) 
    {
        if (pow(-2, 31) <= n && n <= pow(2, 31) - 1)
        {
            if (n == 1)
            {
                return true;
            }
            if (n % 2 == 1 || n <= 0)
            {
                return false;
            }
            return isPowerOfTwo(n/2);
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
    bool result = test.isPowerOfTwo(0);
    cout << result;
    return 0;
}
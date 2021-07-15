#include <iostream>

using namespace std;

class Solution 
{
public:
    int fib(int n)
    {
        if (0 <= n && n <= 30)
        {
            if (n == 0)
            {
                return 0;
            }
            else if (n == 1)
            {
                return 1;
            }
            else
            {
                return fib(n - 1) + fib(n - 2);
            }
        }
        else
        {
            return 0;
        }
    }
};

int main ()
{
    Solution test;
    int result = test.fib(2);
    cout << result;
}
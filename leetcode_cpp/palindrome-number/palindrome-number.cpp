#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

bool isPalindrome(int x)
{   
    // Acceptable Constraints
    if (pow(-2, 31) <= x && x <= pow(2, 31) -1)
    {
        // Do some code
        string value = to_string(x);
        string reversed = to_string(x);
        reverse(reversed.begin(), reversed.end());
        cout << "Reversed value : " << reversed << '\n';

        if (value == reversed)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}

int main()
{   
    bool test = isPalindrome(10);
    cout << test;
    return 0;
}
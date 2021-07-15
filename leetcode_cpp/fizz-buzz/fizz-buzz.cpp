#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

// Return type pointer to the array.
vector<string> fizzbuzz(int n)
{
    if (1 <= n || n <= pow(10, 4))
    {
        vector <string> output(n);
        string value;
        for (int i = 1; i < n + 1; i++) // Loop through and put values in vector
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                value = "FizzBuzz";
            }

            else if (i % 3 == 0)
            {
                value = "Fizz";
            }

            else if (i % 5 == 0)
            {
                value = "Buzz";
            }

            else 
            {
                value = to_string(i);
            }

            cout << "index[" << i - 1 << "] = " << value << '\n';
            output[i-1] = value;
        }
        return output;
    }
    else
    {
        return vector<string>();
    }
}

int main ()
{   
    int num = 15;
    vector <string> test = fizzbuzz(num);

    return 0;
}


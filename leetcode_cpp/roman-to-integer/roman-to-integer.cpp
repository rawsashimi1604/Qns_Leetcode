#include <iostream>
#include <string>

using namespace std;

class Solution
{
    public:
        int romanToInt(string s)
        {
            const int MAXLEN = 15;
            const int MINLEN = 1;
            char ALLOWED[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
            if (MINLEN <= s.length() && s.length() <= MAXLEN)
            {
                
                return 0;
            }
            
            
            return 0;
        }
};

int main()
{
    return 0;
}
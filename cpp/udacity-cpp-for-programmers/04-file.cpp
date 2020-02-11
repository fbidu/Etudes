#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    string line;
    fstream input;

    input.open("test.txt");

    if (input.is_open())
    {
        while (getline(input, line))
        {
            cout << line << '\n';
        }

        input.close();
    }

    int i = 0;
    fstream counter;

    counter.open("counter.txt", ios::app);

    for (i = 0; i < 100; i++)
    {
        counter << i << '\n';
    }

    counter.close();
}
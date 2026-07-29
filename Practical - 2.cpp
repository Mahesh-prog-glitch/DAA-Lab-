#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

// Linear Search
int findLinear(const vector<int>& numbers, int target)
{
    int position = -1;

    for (size_t i = 0; i < numbers.size(); i++)
    {
        if (numbers[i] == target)
        {
            position = i;
            break;
        }
    }

    return position;
}

// Binary Search
int findBinary(const vector<int>& numbers, int target)
{
    int left = 0;
    int right = numbers.size() - 1;

    while (left <= right)
    {
        int center = (left + right) / 2;

        if (numbers[center] == target)
        {
            return center;
        }
        else if (target > numbers[center])
        {
            left = center + 1;
        }
        else
        {
            right = center - 1;
        }
    }

    return -1;
}

int main()
{
    const int SIZE = 100000;
    vector<int> numbers(SIZE);

    // Store sorted values
    for (int i = 0; i < SIZE; i++)
    {
        numbers[i] = i + 1;
    }

    int target;
    cout << "Enter the value to search: ";
    cin >> target;

    int result;

    // Measure Linear Search
    auto begin = high_resolution_clock::now();
    result = findLinear(numbers, target);
    auto finish = high_resolution_clock::now();

    cout << "\n Linear Search " << endl;

    if (result >= 0)
        cout << "Value found at index: " << result << endl;
    else
        cout << "Value not found." << endl;

    cout << "Execution Time: "
         << duration_cast<microseconds>(finish - begin).count()
         << " microseconds" << endl;

    // Measure Binary Search
    begin = high_resolution_clock::now();
    result = findBinary(numbers, target);
    finish = high_resolution_clock::now();

    cout << "\n Binary Search " << endl;

    if (result >= 0)
        cout << "Value found at index: " << result << endl;
    else
        cout << "Value not found." << endl;

    cout << "Execution Time: "
         << duration_cast<microseconds>(finish - begin).count()
         << " microseconds" << endl;

    return 0;
}

OUTPUT:
Enter the value to search: 152

----- Linear Search -----
Value found at index: 151
Execution Time: 2 microseconds

----- Binary Search -----
Value found at index: 151
Execution Time: 1 microseconds


=== Code Execution Successful ===

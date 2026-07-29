#include <iostream>
#include <chrono>
using namespace std;

// Iterative Method
// Time Complexity: O(n)
// Space Complexity: O(1)
unsigned long long iterativeFactorial(int number) {
    unsigned long long factorial = 1;
    for (int count = 2; count <= number; count++) {
        factorial *= count;
    }
    return factorial;
}

// Recursive Method
// Time Complexity: O(n)
// Space Complexity: O(n) because of recursive calls
unsigned long long recursiveFactorial(int number) {
    if (number == 0 || number == 1) return 1;
    return number * recursiveFactorial(number - 1);
}

int main() {
    int value;
    cout << "Enter a non-negative integer: ";
    if (!(cin >> value) || value < 0) {
        cout << "Error: Please enter a valid non-negative integer." << endl;
        return 1;
    }

    // Measure execution time for Iterative Method
    auto iterativeStart = chrono::high_resolution_clock::now();
    unsigned long long iterativeAnswer = iterativeFactorial(value);
    auto iterativeEnd = chrono::high_resolution_clock::now();
    chrono::duration<double, nano> iterativeTime = iterativeEnd - iterativeStart;

    // Measure execution time for Recursive Method
    auto recursiveStart = chrono::high_resolution_clock::now();
    unsigned long long recursiveAnswer = recursiveFactorial(value);
    auto recursiveEnd = chrono::high_resolution_clock::now();
    chrono::duration<double, nano> recursiveTime = recursiveEnd - recursiveStart;

    // Display Results
    cout << "\nFactorial Results" << endl;
    cout << "Input Number : " << value << endl;

    cout << "\nIterative Method" << endl;
    cout << "Factorial : " << iterativeAnswer << endl;
    cout << "Execution Time : " << iterativeTime.count() << " ns" << endl;

    cout << "\nRecursive Method" << endl;
    cout << "Factorial : " << recursiveAnswer << endl;
    cout << "Execution Time : " << recursiveTime.count() << " ns" << endl;

    return 0;
}

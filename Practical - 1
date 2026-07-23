#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
#include <functional>
#include <string>

using namespace std;
using namespace std::chrono;

// 1. Bubble Sort (Optimized with early exit)
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // If no two elements were swapped, the array is already sorted
        if (!swapped) break;
    }
}

// 2. Selection Sort (Standard)
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        if (min_idx != i) {
            swap(arr[i], arr[min_idx]);
        }
    }
}

// 3. Insertion Sort (Standard)
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// 4. Merge Sort (Optimized: Zero dynamic allocations inside the loop)
void merge(vector<int>& arr, vector<int>& temp, int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    
    // Copy back to original array
    for (int p = l; p <= r; p++) {
        arr[p] = temp[p];
    }
}

void mergeSortHelper(vector<int>& arr, vector<int>& temp, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSortHelper(arr, temp, l, m);
        mergeSortHelper(arr, temp, m + 1, r);
        merge(arr, temp, l, m, r);
    }
}

void mergeSort(vector<int>& arr) {
    vector<int> temp(arr.size()); // Allocate memory EXACTLY once
    mergeSortHelper(arr, temp, 0, arr.size() - 1);
}

// 5. Quick Sort (Optimized: Hoare's Partition Scheme + Middle Pivot)
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[low + (high - low) / 2]; 
    int i = low - 1;
    int j = high + 1;
    
    while (true) {
        do { i++; } while (arr[i] < pivot);
        do { j--; } while (arr[j] > pivot);
        if (i >= j) return j;
        swap(arr[i], arr[j]);
    }
}

void quickSortHelper(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortHelper(arr, low, pi);
        quickSortHelper(arr, pi + 1, high);
    }
}

void quickSort(vector<int>& arr) {
    quickSortHelper(arr, 0, arr.size() - 1);
}

// Helper lambda to measure execution time
void benchmark(const string& name, const vector<int>& originalData, function<void(vector<int>&)> sortFunc) {
    vector<int> dataCopy = originalData; 
    
    auto start = high_resolution_clock::now();
    sortFunc(dataCopy);
    auto stop = high_resolution_clock::now();
    
    auto duration = duration_cast<microseconds>(stop - start).count();
    
    // Formatting output for alignment
    cout.width(18); cout << left << name << ": " 
         << duration << " microseconds\n";
}

int main() {
    // Increased n to 10,000. 100 is too small to measure CPU time accurately.
    const int n = 10000; 

    // Modern C++ random number generation
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 10000);

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i] = distrib(gen);
    }

    cout << "Number of Elements = " << n << "\n";
  

    benchmark("Bubble Sort", arr, bubbleSort);
    benchmark("Selection Sort", arr, selectionSort);
    benchmark("Insertion Sort", arr, insertionSort);
    
    benchmark("Merge Sort", arr, mergeSort);
    benchmark("Quick Sort", arr, quickSort);
    
    // Comparing against C++ Standard Library Sort (Introsort)
    benchmark("std::sort (Baseline)", arr, [](vector<int>& a){ sort(a.begin(), a.end()); });

    return 0;
}

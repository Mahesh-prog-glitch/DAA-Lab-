#include <iostream>
#include <vector>
#include <chrono>
using namespace std;

// Heapify function
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

// Build Max Heap
void buildMaxHeap(vector<int>& arr) {
    int n = arr.size();

    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

// Insert into Max Heap
void insertElement(vector<int>& heap, int value) {
    heap.push_back(value);
    int i = heap.size() - 1;

    while (i > 0) {
        int parent = (i - 1) / 2;

        if (heap[parent] < heap[i]) {
            swap(heap[parent], heap[i]);
            i = parent;
        } else {
            break;
        }
    }
}

// Delete Maximum Element
int deleteMax(vector<int>& heap) {
    if (heap.empty()) {
        return -1;
    }

    int maximum = heap[0];

    heap[0] = heap.back();
    heap.pop_back();

    if (!heap.empty()) {
        heapify(heap, heap.size(), 0);
    }

    return maximum;
}

// Display Heap
void displayHeap(const vector<int>& heap) {
    for (int value : heap) {
        cout << value << " ";
    }
    cout << endl;
}

// ---------------- Main Program ----------------
int main() {
    int n;

    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> arr(n);

    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    auto startTime = chrono::high_resolution_clock::now();

    // Build Heap
    buildMaxHeap(arr);

    cout << "\nMax Heap: ";
    displayHeap(arr);

    // Insert
    int value;
    cout << "\nEnter element to insert: ";
    cin >> value;

    insertElement(arr, value);

    cout << "Heap after insertion: ";
    displayHeap(arr);

    // Delete Maximum
    int deleted = deleteMax(arr);

    cout << "Deleted Maximum Element: " << deleted << endl;

    cout << "Heap after deletion: ";
    displayHeap(arr);

    auto endTime = chrono::high_resolution_clock::now();

    chrono::duration<double> executionTime = endTime - startTime;

    cout << "\nExecution Time: "
         << executionTime.count()
         << " seconds" << endl;

    return 0;
}

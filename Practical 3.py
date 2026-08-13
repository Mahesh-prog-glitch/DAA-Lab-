import time


# Heapify function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Build Max Heap
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# Insert into Max Heap
def insert(heap, value):
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break


# Delete Maximum Element
def delete_max(heap):
    if len(heap) == 0:
        return None

    maximum = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    if len(heap) > 0:
        heapify(heap, len(heap), 0)

    return maximum


# ---------------- Main Program ----------------
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    arr = list(map(int, input("Enter the elements: ").split()))

    if len(arr) != n:
        print("Error: Number of elements entered does not match.")
    else:
        start_time = time.perf_counter()

        # Build Heap
        build_max_heap(arr)
        print("\nMax Heap:", arr)

        # Insert
        value = int(input("\nEnter element to insert: "))
        insert(arr, value)
        print("Heap after insertion:", arr)

        # Delete Maximum
        deleted = delete_max(arr)
        print("Deleted Maximum Element:", deleted)
        print("Heap after deletion:", arr)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print("\nExecution Time: {:.8f} seconds".format(execution_time))

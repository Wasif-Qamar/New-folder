import time
import random

# Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure time
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())  # Use a copy to avoid in-place sorting
    return time.time() - start_time

# Create Arrays
n = 1000  # Array size
array1 = list(range(n))  # Already sorted
array2 = random.sample(range(n), n)  # Randomly shuffled
array3 = list(range(n, 0, -1))  # Sorted in descending order

# Measure performance
results = {}

for sort_func, name in [(bubble_sort, "Bubble Sort"), 
                        (selection_sort, "Selection Sort"),
                        (merge_sort, "Merge Sort"), 
                        (quick_sort, "Quick Sort")]:
    
    results[name] = {
        "Best Case": measure_time(sort_func, array1),
        "Average Case": measure_time(sort_func, array2),
        "Worst Case": measure_time(sort_func, array3)
    }

# Print results
for sort_name, cases in results.items():
    print(f"{sort_name}:")
    for case, time_taken in cases.items():
        print(f"  {case}: {time_taken:.6f} seconds")

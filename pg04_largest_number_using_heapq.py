# import heapq

# def find_largest(nums):
#     return heapq.nlargest(1, nums)[0]

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# largest_number = find_largest(numbers)
# print("The largest number is:", largest_number)

#without library
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


# Build max heap from array
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


# Find the largest element
def find_largest(arr):
    arr = arr[:]          
    build_max_heap(arr)
    return arr[0]


nums = [10, 4, 7, 1, 9, 20]
print("Largest element:", find_largest(nums))


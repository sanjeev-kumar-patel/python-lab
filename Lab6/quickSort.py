## Pivot is at last

# def partition(arr, low ,high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low,high):
#         if(arr[j] < pivot):
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i+1

# def quick_sort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)

#         quick_sort(arr, low, p - 1)
#         quick_sort(arr, p + 1, high)


# arr = [10, 20, 100, 21, 9, -2]

# quick_sort(arr, 0, len(arr) - 1)

# print(arr)

## Pivot is at beginning 

# def partition(arr, low, high):
#     pivot = arr[low]

#     i = low + 1
#     j = high

#     while i <= j:

#         while i <= high and arr[i] <= pivot:
#             i += 1

#         while j >= low and arr[j] > pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[low], arr[j] = arr[j], arr[low]

#     return j


# def quick_sort(arr, low, high):
#     if low < high:
#         p = partition(arr, low, high)

#         quick_sort(arr, low, p - 1)
#         quick_sort(arr, p + 1, high)


# arr = [10, 20, 100, 21, 9, -2]

# quick_sort(arr, 0, len(arr) - 1)

# print(arr)


## Using List Comprehension

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [10, 20,10,20, 100, 21, 9, -2]

print(quick_sort(arr))
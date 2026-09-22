arr = [4, 5, 3, 20, 6, 9]
def heapify(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    parent = i
    if left < n and arr[left] > arr[parent]:
        parent = left

    if right < n and arr[right] > arr[parent]:
        parent = right

    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]

        heapify(arr, parent, n)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, 0, i)

heap_sort(arr)
print(arr)
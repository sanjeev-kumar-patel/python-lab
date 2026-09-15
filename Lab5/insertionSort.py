# Q2. c) Insertion Sort

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                break

            j = j - 1

        arr[j + 1] = key

    print(arr)


arr = [1, 2, 43, 1, 4, 2, 1, -1, -19]
insertionSort(arr)
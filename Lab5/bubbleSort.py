# Q1. Sorting 
# a) Bubbble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    
arr = [1,34,2,4,3,6,2,6,-6,1,0,-5]
bubbleSort(arr)
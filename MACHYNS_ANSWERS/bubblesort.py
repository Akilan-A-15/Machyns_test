# 2)    [2,1,5,7,3,9,0] sort given list using bubble sort method.?
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [2, 1, 5, 7, 3, 9, 0]
bubble_sort(arr)
print("Sorted array:", arr)

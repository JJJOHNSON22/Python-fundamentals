# Python program for implementation of Bubble Sort 

def bubbleSort(arr): 
    ilen = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True 
        for i in range(0, ilen): 
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i] 
    return arr

list1 = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(list1)) 
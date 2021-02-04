def selectionSort(arr):
    ilen = range(0, len(arr) - 1)
    for i in ilen:
        min = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]

    return arr


list1 = [8, 5, 7, 2, 3, 1]
print(selectionSort(list1)) 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

data = [3, 9, 6, 5, 11]
print("Original list :", data)
print("Selection Sort:", selection_sort(data.copy()))

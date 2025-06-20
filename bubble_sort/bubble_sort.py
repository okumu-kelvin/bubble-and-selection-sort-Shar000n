def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break
    return unsorted_list

data = [6,5, 1, 2, 7]

print("Original list :", data)
print("Bubble Sort:", bubble_sort(data.copy()))

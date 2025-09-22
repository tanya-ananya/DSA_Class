def sequential_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def binary_search(arr, target):
    if arr is None or len(arr) == 0:
        return -1
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

def bubble_sort(arr):
    if arr is None:
        return None
    elif len(arr) == 1:
        return arr
    
    n = len(arr)
    for x in range(n):
        swapped = False
        for y in range(0, n-x-1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for x in range(1, len(arr)):
        key = arr[x]
        y = x - 1
        while y >= 0 and key < arr[y]:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
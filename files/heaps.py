def maxHeapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)

def maxSort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    for x in range(n//2 - 1, -1, -1):
        maxHeapify(arr, n, x)

    for x in range(n - 1, 0, -1):
        arr[x], arr[0] = arr[0], arr[x]
        maxHeapify(arr, x, 0)
    return arr

def minHeapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, n, smallest)

def minSort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    for x in range(n//2 - 1, -1, -1):
        minHeapify(arr, n, x)
    for x in range(n - 1, 0, -1):
        arr[x], arr[0] = arr[0], arr[x]
        minHeapify(arr, x, 0)
    return arr
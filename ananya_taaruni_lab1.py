import sys
import timeit

# Part A: Sum of n Numbers in an Array
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total

print()
print('Part A: Sum of n Numbers in an Array')
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(timeit.timeit(lambda: sum_array(arr), number=100))
print(f'Size of array: {sys.getsizeof(arr)}')
print()

# Part B: Matrix Addition
def matrix_addition(mat_one, mat_two):
    total = 0
    for i in range(len(mat_one)):
        for j in range(len(mat_one[0])):
            total += mat_one[i][j] + mat_two[i][j]
    return total

print()
print('Part B: Matrix Addition')
arr1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
arr2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
print(timeit.timeit(lambda: matrix_addition(arr1, arr2), number=100))
print(f'Size of array: {sys.getsizeof(arr1, arr2)}')
print()

print("Report: \n")
print("Part A is a simple iterative function adding the input array's numbers. The time complexity of this function is O(n) and space complexity is O(1). This algorithm is efficient as it doesn't store many values and runs with each iteration of the array as O(n)\n")
print("Part B is an iterative function going through the matrix for each number and adding it to the total. The time complexity is O(n^2) and space complexity is O(1). The function is efficient because it    has optimal space storage and runs with each input.\n")

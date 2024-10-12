def bubble_sorting(integers):
    n = len(integers)
    for i in integers:
        for j in range(0, n-1):
            if integers[j] > integers[j+1]:
                integers[j], integers[j+1] = integers[j+1], integers[j]
    return (integers)
print(bubble_sorting([1, 8, 7, 6, 5, 4, 3, 2, 9, 11, 17, 20, 12, 14, 13, 15, 16, 10, 19, 18]))
print(bubble_sorting([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(bubble_sorting([1, 3, 2]))
print(bubble_sorting([1, 7, 8, 100]))
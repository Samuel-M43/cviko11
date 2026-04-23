import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


random.seed(42)
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort(values):
    vystup = values.copy()
    n = len(values)
    for i in range(n):
        min_idx = i
        for k in range(i + 1, n):
            if values[k] < values[min_idx]:
                min_idx = k
        vystup[i], vystup[min_idx] = vystup[min_idx], vystup[i]

    return vystup

#print(selection_sort(values))

import matplotlib.pyplot as plt

def bubble_sort(values):
    n = len(values)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break
    return values


print(bubble_sort(values))




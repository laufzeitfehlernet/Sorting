import random

def selection_sort(a):

    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
   
    return a

if __name__ == "__main__":
    data = [random.randint(0, 1000) for _ in range(random.randint(0, 50))]

    print(data)
    print(selection_sort(data))


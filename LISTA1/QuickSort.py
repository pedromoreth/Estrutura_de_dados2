import random
import time


def partition(array, l, r):
    pivot = array[l]  # escolhe o 1º elemento como pivô
    i = l+1
    for j in range(l+1, r):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[l], array[i-1] = array[i-1], array[l]
    return i-1


def random_partition(array, l, r):
    i = random.randrange(l, r)
    array[l], array[i] = array[i], array[l]
    return partition(array, l, r)


def quick_sort(array, l, r):
    if l < r:
        p = partition(array, l, r)
        quick_sort(array, l, p)
        quick_sort(array, p+1, r)


if __name__ == "__main__":
    lst = random.choices(range(100), k=50)

    #saidas
    print('entrada: ', lst)
    start = time.time()
    quick_sort(lst, 0, len(lst))
    print('QuickSorted:', lst)
    end = time.time()
    print(format(end-start),'segundos')
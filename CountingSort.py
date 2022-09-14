import random
import time

def counting_sort(seq):
    if len(seq) > 1:
        return _counting_sort(seq)
    return seq


def _counting_sort(seq):
    counts = [0 for _ in range(max(seq) + 1)]

    for element in seq:
        counts[element] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]

    sorted_seq = [0 for _ in range(len(seq))]
    for element in seq:
        counts[element] -= 1
        sorted_seq[counts[element]] = element

    return sorted_seq



if __name__ == "__main__":
    lst = random.choices(range(1000), k=50)

    #saidas
    print('entrada: ', lst)
    start = time.time()
    print('CountingStord:', counting_sort(lst))
    end = time.time()
    print(format(end-start),'segundos')

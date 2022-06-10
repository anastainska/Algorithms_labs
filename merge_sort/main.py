import sys
import time

comparisons = 0
execution_time = 0


def merge(array_one, array_two):
    array_temp = []
    global order
    global comparisons

    if order == 'asc':
        while len(array_one) != 0 and len(array_two) != 0:
            if array_one[0] > array_two[0]:
                array_temp.append(array_two[0])
                array_two.pop(0)
                comparisons = comparisons + 1
            elif array_one[0] <= array_two[0]:
                array_temp.append(array_one[0])
                array_one.pop(0)
                comparisons = comparisons + 1
    elif order == 'desc':
        while len(array_one) != 0 and len(array_two) != 0:
            if array_one[0] > array_two[0]:
                array_temp.append(array_one[0])
                array_one.pop(0)
                comparisons = comparisons + 1
            elif array_one[0] <= array_two[0]:
                array_temp.append(array_two[0])
                array_two.pop(0)
                comparisons = comparisons + 1
    else:
        print("Pls choose the right order asc/desc")
        return

    while len(array_one) != 0:
        array_temp.append(array_one[0])
        array_one.pop(0)

    while len(array_two) != 0:
        array_temp.append(array_two[0])
        array_two.pop(0)

    return array_temp


def mergesort(array_unsorted, order):
    if len(array_unsorted) == 1:
        return array_unsorted
    length_array = len(array_unsorted)
    middle_index = length_array // 2
    array_a = array_unsorted[:middle_index]
    array_b = array_unsorted[middle_index:]

    array_a = mergesort(array_a, order)
    array_b = mergesort(array_b, order)

    return merge(array_a, array_b)


if __name__ == '__main__':
    order = sys.argv[1]
    array_test = list(map(int, sys.argv[2].split(',')))
    start_time = time.time()
    array_test = mergesort(array_test, order)
    end_time = time.time()
    print("MergeSort: " + str(array_test))
    print("Comparisons: " + str(comparisons))
    print("Swaps: btw merge has no swaps :| ")
    print("Execution time: %s seconds" % (end_time - start_time))

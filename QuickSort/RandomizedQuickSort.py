import random

def QuickSort(array, start, end):

    if end <= start:
        return 
    
    pivot = rand_partition(array, start, end)

    QuickSort(array, start, pivot - 1)
    QuickSort(array, pivot + 1, end)

    return array

def rand_partition(array, start, end):
    randomPivot = random.randrange(start, end)

    array[start], array[randomPivot] = array[randomPivot], array[start]
    return partition(array, start, end)


def partition(array, start, end):
    pivot_value = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] < pivot_value:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    i += 1

    temp = array[i]
    array[i] = array[end]
    array[end] = temp

    return i

def is_array_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
        
    return True

if __name__ == "__main__":
    arr = [random.randint(1, 20) for _ in range(20)]

    print("Original array:", arr)
    print("Sorted:", is_array_sorted(arr))

    QuickSort(arr, 0, len(arr) -1)
    print("\n")

    print("Sorted array:",arr)
    print("Sorted:", is_array_sorted(arr))
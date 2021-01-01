# time complexity : O(n²)

def bubble_sort(array):
    """
    Sorts the passed array using bubble sort 
    technique
    """
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


if __name__ == "__main__":
    # you can also read input from stdin
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Before Sorting:", *array)
    array = bubble_sort(array)
    print("After Sorting:", *array)

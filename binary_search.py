def binary_search(array: list[int], key: int, /) -> int:
    """

    binary_search(..)
        binary_search(array: list[int], key: int, /) -> int

        Return the index in array where key is found.

        Return -1 on failure.

    """
    n = len(array)
    first, last, mid = 0, n-1, (n-1)//2
    while first < last:
        # if the element is found return its index.
        if array[mid] == key:
            return mid
        # if the middle element is less than key ASSIGN mid to last
        elif key < array[mid]:
            last = mid - 1
        # middle element is greater than key,then assign mid to first
        else:
            first = mid + 1
        # Compute middle element.
        mid = (first + last)//2
    # if element not found
    return -1


if __name__ == "__main__":
    # print(help(binary_search))
    array = [int(x) for x in input().split()]
    key = int(input("Enter element to find: "))
    index = binary_search(array, key)
    if index != -1:
        print("Element %d found at index %d" % (key, index))
    else:
        print("Element %d not found" % (key))

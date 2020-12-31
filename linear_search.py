def linear_search(array, key):
    """
    returns the index position of "key"
    in the array if present
    else -1
    """
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1
if __name__ == "__main__":
    # You Can read input from stdin here
    # array = list(map(int,input().split()))
    # key = int(input())
    array = [1,2,3,4,5,6,7,8,9,10]
    key = 8
    index = linear_search(array, key)
    if index == -1:
        print("Element Not Present in the array")
    else:
        print("Element present at index %d of the array"%index)
    

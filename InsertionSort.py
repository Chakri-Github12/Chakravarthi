'''
    Time Complexity:
        Best Case : O(n)
        Worst Case: O(n²)
        Average   : O(n²)
'''
def insertion_sort(array, n):
    
    for i in range(1, n):
        j = i - 1
        key = array[i]
        while (j >= 0 ) and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
if __name__ == "__main__":
    array = [8,6,4,2,0,9,7,5,3,1]
    print("Before Sorting:",*array)
    array = insertion_sort(array, len(array))
    print("After Sorting:",*array)
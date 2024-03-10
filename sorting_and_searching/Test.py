
def mergeTwoSortedArray(array1, array2,  myArray):
    arr1Pointer = 0
    arr2Pointer = 0
    myArrayPointer = 0
    while(arr1Pointer < len(array1) and arr2Pointer < len(array2)):
        if array1[arr1Pointer] <= array2[arr2Pointer]:
            myArray[myArrayPointer] = array1[arr1Pointer]
            arr1Pointer += 1
        else:
            myArray[myArrayPointer] = array2[arr2Pointer]
            arr2Pointer += 1
        myArrayPointer += 1
    while arr1Pointer < len(array1):
        myArray[myArrayPointer] = array1[arr1Pointer]
        myArrayPointer += 1
        arr1Pointer += 1
    while arr2Pointer < len(array2):
        myArray[myArrayPointer] = array2[arr2Pointer]
        myArrayPointer += 1
        arr2Pointer += 1


def mergeSort(myArray):
    if len(myArray) <= 1:
        return 
    midPoint = len(myArray) // 2
    leftSide = myArray[:midPoint]
    rightSide = myArray[midPoint:]
    mergeSort(leftSide)
    mergeSort(rightSide)
    mergeTwoSortedArray(leftSide, rightSide, myArray)



unsorted_array = [5, 1, 4, 2, 8, 3, 7, 6]
mergeSort(unsorted_array)
expected_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
print(unsorted_array)


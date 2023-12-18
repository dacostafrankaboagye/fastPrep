'''

    pivotElement = firstELement
    we want to put in its position

    // in doing so we partion the arr - (all the elements on the left side of the pivot Element, are less than it ; all the element to the right of the pivot ELment are greater than it)

    // if the pivot Element is in the right position:
    we have
                (left elements) (the pivot element) (right elements)

-> focus on the left elements
    => repeat the same process


Partioning Schemes

1. Hoare Partioning
2. Lomuto Partioning 


Hoare Partioning - invented quick sort

            pivotElement = first one
            startPointer = the second one
            endPointer = last one

            From the startPointer => move => we want the element > than the pivot element
            = stop once you find it

            From the endPointer => move => we want the element < than the pivot element
            = stop once you find it

            => swap the result (swap the startPointer and the endPointer)
            => contine the process until startPointer crosses the endPointer 

            > if that happens, 
                => swap the enPointer and the pivot element 


            // now the pivot element is in its place


Lomuto partioning 
- its something





Average time complexity = O(nlogn)
    -> lets say, we are reducing by proportions -> anytime we partion, the space at the left and right is reduced by two - order of log n
worst time complexity = O(n^2)
    -> if the list is already sorted
    -> we are not really reducing the search space
    -> for each element we are performing n- iterations
    -> and there are n elements in total

- for smaller list





'''

def swap(a,b,arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(list_of_numbers, startIndex, endIndex):
    pivot_index = startIndex
    pivot_element = list_of_numbers[pivot_index]


    while startIndex < endIndex:

        # move start (we want to find an element > than the pivot element)
        while  startIndex <= endIndex and list_of_numbers[startIndex] <= pivot_element:
            startIndex += 1

        # move end (we want to find an element < than the pivot element)
        while endIndex >= startIndex and list_of_numbers[endIndex] > pivot_element:
            endIndex -= 1

        if startIndex < endIndex : swap(startIndex, endIndex, list_of_numbers) 

    swap(endIndex, pivot_index, list_of_numbers)
    return endIndex

    



def quick_sort(list_of_numbers, startIndex, endIndex):

    if startIndex < endIndex:
    
        # put the element in their right position
        partionIndex = partition(list_of_numbers, startIndex, endIndex )
        
        quick_sort(list_of_numbers, startIndex, partionIndex-1)

        quick_sort(list_of_numbers, partionIndex +1, endIndex)


if __name__ == '__main__':
    list_of_numbers = [11, 9, 28, 7, 2, 15, 28]
    tests = [
        [11, 9, 28, 7, 2, 15, 28],
        [9,0],
        [1,2,4,5,8,0],
        [],
        [9,0,0]
    ]
    for list_of_numbers in tests:
        quick_sort(list_of_numbers, startIndex=0, endIndex=len(list_of_numbers)-1)
        print(f"sorted arr = {list_of_numbers}")
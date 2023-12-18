'''
know how to merget two sorted list - create a function for it  -  return the sorted arr
 - set a pointer to the first list and the second list
 - compare the pointer elements
 - append to a new list

 - some lements will be left though
    - loop through and add them as well


- create your merge sort funx - its going to be recurssive
- we break the array down till we get of size 1 - base condition
 
- divid the arr - in the middle
- create the left arr
- crete teh right arr

call merge sort on the left
call merge sort on the right

call the funx for the merge sorted list on both the left and the right and return it



// the above solution required that, we create a new arr - 
can we do better?



def merge_two_sorted_list(list_a, list_b):
    sortedList = []

    len_a = len(list_a)
    len_b = len(list_b)

    a_pointer = b_pointer = 0

    while a_pointer < len_a and b_pointer < len_b:
        if list_a[a_pointer] <= list_b[b_pointer]:
            sortedList.append(list_a[a_pointer])
            a_pointer += 1
        else:
            sortedList.append(list_b[b_pointer])
            b_pointer += 1

    while a_pointer < len_a:
        sortedList.append(list_a[a_pointer])
        a_pointer += 1

    while b_pointer < len_b:
        sortedList.append(list_b[b_pointer])
        b_pointer += 1
    
    return sortedList


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_side = merge_sort(left_arr)
    right_side = merge_sort(right_arr)

    return merge_two_sorted_list(left_side, right_side)



if __name__ == '__main__':
    arr = [11, 9, 28, 7, 2, 15, 28]
    tests = [
        [11, 9, 28, 7, 2, 15, 28],
        [9,0],
        [1,2,4,5,8,0],
        [],
        [9,0,0]
    ]
    for arr in tests:
        result = merge_sort(arr)
        print(f"sorted arr = {result}")



# # test merge_two_sorted
# result = merge_two_sorted_list([3, 10, 29], [2, 19, 100])
# print(f'sorted = {result}')


'''


# removing the list - storage to make it efficient
        
def merge_two_sorted_list(list_a, list_b, arr):

    len_a = len(list_a)
    len_b = len(list_b)

    a_pointer,b_pointer, arr_pointer = 0, 0 , 0

    while a_pointer < len_a and b_pointer < len_b:
        if list_a[a_pointer] <= list_b[b_pointer]:
            arr[arr_pointer] = list_a[a_pointer]
            a_pointer += 1
            
        else:
            arr[arr_pointer] = list_b[b_pointer]
            b_pointer += 1
            
        arr_pointer += 1

    while a_pointer < len_a:
        arr[arr_pointer] = list_a[a_pointer]
        a_pointer += 1
        arr_pointer += 1

    while b_pointer < len_b:
        arr[arr_pointer] = list_b[b_pointer]
        b_pointer += 1
        arr_pointer += 1
    


def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge_two_sorted_list(left_arr, right_arr, arr)



if __name__ == '__main__':
    #arr = [11, 9, 28, 7, 2, 15, 28]
    tests = [
        [11, 9, 28, 7, 2, 15, 28],
        [9,0],
        [1,2,4,5,8,0],
        [9,0,0]
    ]
    for arr in tests:
        merge_sort(arr)
        print(f"sorted arr = {arr}")



# # test merge_two_sorted
# result = merge_two_sorted_list([3, 10, 29], [2, 19, 100])
# print(f'sorted = {result}')





def linear_search(list_of_numbers, number_to_find):
    for index, element in enumerate(list_of_numbers):
        if element == number_to_find:
            return index 
    return -1

def binary_search(list_of_numbers, number_to_find):
    left_index = 0
    right_index = len(list_of_numbers) - 1
    

    while left_index <= right_index:
        middle_index = (right_index + left_index)//2
        middle_element = list_of_numbers[middle_index]
        if middle_element == number_to_find:
            return middle_index 
        if middle_element < number_to_find:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1


def binary_search_with_recurssion(list_of_numbers, number_to_find, left_index, right_index):
    # base case
    if left_index > right_index:
        return -1
    
    middle_index = (right_index + left_index)//2
    middle_element = list_of_numbers[middle_index]

    if middle_element == number_to_find:
        return middle_index 
    
    if middle_element < number_to_find:
        left_index = middle_index + 1
    else:
        right_index = middle_index - 1

    return binary_search_with_recurssion(list_of_numbers, number_to_find, left_index, right_index)



if __name__ == '__main__':
    list_of_numbers = [3, 7, 9, 10, 40, 55, 98, 671]
    number_to_find = 671

    index = binary_search_with_recurssion(list_of_numbers, number_to_find, 0, len(list_of_numbers)-1)
    print(f"at index = {index}")

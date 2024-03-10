

'''
we take two consecutive elements and compare
- we swap aterwards

time complexity = O(n^2)
space complexity = O(1)

Note: 
outer loop = [(size of arr - 1)] or [(size of arr)]
inner loop = [(size of arr - 1)]
 - after say, the first two iterations, the last two is sorted: 
     - so you will need to run the inner loop [(size of arr - 1)] - the iteration position of the outer loop
    - len(list_of_numbers)-1 - i  : if i was the outer loop iterator variable

    

'''

# start 
'''
def bubble_sort(list_of_numbers):

    for k in range(len(list_of_numbers)):

        for i in range(len(list_of_numbers)-1 ):
            if list_of_numbers[i] > list_of_numbers[i+1]:
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
'''



# dealing with the inner loop
'''
def bubble_sort(list_of_numbers):

    for k in range(len(list_of_numbers)):

        for i in range(len(list_of_numbers)-1 - k):
            if list_of_numbers[i] > list_of_numbers[i+1]:
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
'''



'''
what if the list is sorted already?
- does it have to do the operations again!
- is there a way to determine that is sorted?
    - Yes! -> if we go through the inner loop and we do not swap anything -> then it means its already sorted
'''


def bubble_sort(list_of_numbers):

    swapped = False

    for k in range(len(list_of_numbers)):

        for i in range(len(list_of_numbers)-1 - k):
            if list_of_numbers[i] > list_of_numbers[i+1]:
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
                swapped = True
        if swapped:
            break



if __name__ == '__main__':
    # list_of_numbers = [100, 9, 3, 0, 1, 89, 10]
    list_of_numbers = [9, 80, 76, 430, 990]
    bubble_sort(list_of_numbers)
    print(f"sorted list = {list_of_numbers}")
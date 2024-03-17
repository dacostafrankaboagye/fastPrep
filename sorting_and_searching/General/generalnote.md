## Bubble Sort

    Also called "sinking sort"

    The largest element tend to sink at the end of the array - with each iteration

    Take adjacent pairs - compare them - swap if necessary (in the wrong order)

    At the end of each pass / iteration, you do not add the last element
    (why?-> the last element will be at the correct position.
    Remember-> the largest element tend to sink at the end of the array)

    How do  we know when it's done sorting? ->  When there are no more swaps in a pass -> so keep track of the swapping

```java

public void bubbleSort(int[] arr){
    int arrLength = arr.length;
    boolean swappingHasOccured;
    for(int i=0; i<arrLength-1; i++){
        swappingHasOccured = false;
        for(int j=0; j<arrLength -1 -i; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swappingHasOccured = true;
            }
        }
        if(swappingHasOccured == false){break;}
    }

}

```

---

## Insertion Sort

    Works like the way we sort playing cards in our hands

    - divide the given array into two parts
        - sorted and unsorted part

    Sorting partition  |
                       V
                      [3, 1, 5, 2, 6]

    - one element in the sorted part

    From the unsorted part, take the first element -> place it in the correct position in the sorted array (based on some logic)
        - all the elements in the sorted array greater than the "first element we picked" -> shifts by one position

    - take the first element from the unsorted array
    - compare the element with each and every element in the sorted array
    - any element in the sorted array which is greater than the "first element" we picked-> shifts by one position
    - if we encounter an element which is lesser than the "first element" we picked -> place the "first element" right after it
    repeat till unsorted array is not empty

    : dividing the unsorted array
        - pick the first element -> that is sorted
        -> the rest is unsorted
        -> // implement
        -> pick the first two -> that is sorted
        -> the rest is unsorted
        -> // implement
        ...
        When comparing start from behind
        ...

```java
public void insertionSort(int[] arr){
    int n = arr.length;
    for(int i=1; i < n; i++){
        int temp = arr[i];
        int j = i - 1;
        while(j>=0 && arr[j] > temp){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = temp;
    }
}

```

---

## Selection Sort

    divide the array into two part - sorted part, unsorted part

    Sorting partition |
                      V
                      [3, 1, 5, 2, 6]

    - no element in the sorted part
    - find the minimum element (its index) among the element in the unsorted part
    - once the minimum is found -> swap it with the leftmost element of the partition / boundary
        - once we do this, -> we know the minimum element is at the correct position -> it becomes part of the sorted array
    - we repeat till all the elements are part of the sorted array

    - at each pass, one element of the unsorted part becomes part of the sorted part
    - you will notice that after the (n-1) pass, where n is the length if the arr. The entire arr is sorted

```java

public void selectionSort(int[] arr){
    int n = arr.length;
    for(int i=0; i<n-1; i++){
        int min =i;
        for(int j=i+1; j<n; j++){
            if(arr[j] < arr[min]  ){
                min = j;
            }
        }
        // swap
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}

```

---

## Merge Sort

    - divide and conquer algorithm
    - divide
        - divide into two halves - do it recurssively for the two halves until there are no more half arrays to divide - "single element"
    - conquer
        - start from the bottom, sort and merge
        (understand how to merge two sorted array)

    Two things
        - break the array into two recursively - (have a base case)
        - merge two sorted array together (use the help of a temp array of equal length)

    case 1 - when the left array is exhausted
        - (you do not need to push the rest of the right element)
    case 2 - when the right array is exhausted
        - (you need to push the rest of the left elements) : a piece of code for it

    note:
        Initial values
            - low = 0. high = last index temp[] array = same length of the original array - initial values = 0's
        Mid index calculation = low + ((high - low)/2)  ::: (high - low) : we will be in the range :: we want to avoid the overflow of integer value
        base case: low < high

    How to treat it
    - Base Case
        - overflow
        - divide - left, right
        - conquer - merge - (arr, temp, low, mid, high)
                - copy to temp
                - have three pointers

```java

public void sortTwoSortedArray(int[] arr, int[] temp, int low, int mid, int high){
    for(int i=low; i<=high; i++){
        temp[i] = arr[i];
    }
    int i=low;
    int j=mid+1;
    int k=low;
    while(i<=mid && j<=high){
        if(temp[i] < temp[j]){
            arr[k] = temp[i];
            i++;
        }else{
            arr[k] = temp[j];
            j++;
        }
        k++;

    }
    // if the right is exhaused - fill the rest of the left
    while(i<=mid){
        arr[k] = temp[i];
        i++;
        k++;
    }
}

public void mergeSort(int[] arr, int low, int high){
    // base case
    if(low < high){
        // overflow
        int mid = low + ((high - low)/2);
        // divide
            // left
        mergeSort(arr, low, mid);
            //right
        mergeSort(arr, mid+1, high);
        // conquer
        int[] temp = new int[arr.length];
        sortTwoSortedArray(arr, temp, low, mid, high);

    }
}


```

---

## Quick Sort

    - Take a Pivot
        - can be the first element
        - can be the last element
        - can be any random element
    - Partition the array:
        - all element > the pivot -> move to the right
        - all element < the pivot -> move to the left
        - all lement == the pivot -> move to either side

    - Recursion
        - recursively apply the two steps(pivot and partition) above on the left side and the right side

    Note:
     - After we perform the partition, the pivot is at the correct position

```java

```

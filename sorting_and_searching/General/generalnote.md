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
        Time Complexity: O(n^2)


    

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
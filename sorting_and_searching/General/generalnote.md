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
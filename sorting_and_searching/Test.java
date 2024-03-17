import java.util.Arrays;

/*

 * 
 * 
 */

public class Test {

    public void bubbleSort(){
    }

    public void insertionSort(){

    }

    public void selectionSort(){
    }


    public void mergeSort(int[] arr, int low, int high){
    }

    public int partition(int[] arr, int low, int high){
        /*
        low -> j-1 : elements <= pivot
        j -> i-1   : elements > pivot
        i -> high  : elements yet to be traversed
        */
        int i = low;
        int j = low;
        int pivot = arr[high];
        while(i <= high){
            if(arr[i] <= pivot){
                // swap
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;

                j++;
            }
            i++;
        }
        return j-1;
    }

    public void quickSort(int[] arr, int low, int high){

        // base case
        if(low < high){

            int pivotIndex = partition(arr, low, high);
        
            // left
            quickSort(arr, low, pivotIndex-1);

            //right
            quickSort(arr, pivotIndex+1, high);
        }
    }


    public static void main(String[] args) {

        Test myTest = new Test();

        int[] myArr = {3, 1, 10, 2, 1, 99, 1, 0};
        System.out.println("Before: " + Arrays.toString(myArr));
        // myTest.bubbleSort(myArr);
        // myTest.insertionSort(myArr);
        // myTest.selectionSort(myArr);
        // myTest.mergeSort(myArr, 0, myArr.length-1);
        myTest.quickSort(myArr, 0, myArr.length-1);
        System.out.println("After: " + Arrays .toString(myArr));

        Arrays.sort(args);
        

    }

}

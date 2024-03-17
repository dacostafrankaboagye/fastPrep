import java.util.Arrays;

/*

 * 
 * 
 */

public class Test {

    public void bubbleSort(int[] arr){
        boolean swapped;
        int n = arr.length;
        for(int i=0; i<n-1; i++){
            swapped = false;
            for(int j=0; j<n-1-i; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if(swapped == false){break;}
        }

    }

    public void insertionSort(int[] arr){
        int n = arr.length;
        for(int i=1; i<n;i++){
            int temp = arr[i];
            int j = i-1;
            while(j >= 0 && arr[j]>=temp){
                arr[j+1] = arr[j];
                j = j-1;
            }
            arr[j+1] = temp;
        }

    }

    public void selectionSort(int[] arr){
        int n = arr.length;
        for(int i=0; i<n-1; i++){
            int min = i;
            for(int j=i+1; j<n; j++){
                if(arr[min] > arr[j]){
                    min = j;
                }
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }

    }

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




    public static void main(String[] args) {

        Test myTest = new Test();

        int[] myArr = {3, 1, 10, 2, 1, 99, 1, 0};
        System.out.println("Before: " + Arrays.toString(myArr));
        // myTest.bubbleSort(myArr);
        // myTest.insertionSort(myArr);
        // myTest.selectionSort(myArr);
        myTest.mergeSort(myArr, 0, myArr.length-1);
        System.out.println("After: " + Arrays .toString(myArr));

        Arrays.sort(args);
        

    }

}

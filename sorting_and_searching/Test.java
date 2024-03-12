import java.util.Arrays;

/*

 * 
 * 
 */

public class Test {

    public void bubbleSort(int[] arr){
        int n = arr.length;
        boolean swapped;
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
        for(int i = 1; i < n; i++){
            int temp=arr[i];
            int j = i -1;
            while(j>=0 && arr[j] > temp){
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




    public static void main(String[] args) {

        Test myTest = new Test();

        int[] myArr = {3, 1, 10, 2, 1, 99, 1, 0};
        System.out.println("Before: " + Arrays.toString(myArr));
        //myTest.selectionSort(myArr);
        System.out.println("After: " + Arrays.toString(myArr));
        

    }

}

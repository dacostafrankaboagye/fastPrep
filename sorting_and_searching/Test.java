import java.util.Arrays;

public class Test {

    public void bubbleSort(int[] arr){
        boolean swapped;
        for(int i=0; i<arr.length - 1; i++){
            swapped = false;
            for(int j=0; j<arr.length-1-i; j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if(swapped == false){break;}
        }

    }

    public static void main(String[] args) {

        Test myTest = new Test();

        int[] myArr = {3, 1, 10, 2, 1, 99, 1, 0};
        System.out.println("Before: " + Arrays.toString(myArr));
        myTest.bubbleSort(myArr);
        System.out.println("After: " + Arrays.toString(myArr));
        

    }

}

import java.util.Arrays;

public class Test {

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

    public static void main(String[] args) {

        Test myTest = new Test();

        int[] myArr = {3, 1, 10, 2, 1, 99, 1, 0};
        System.out.println("Before: " + Arrays.toString(myArr));
        myTest.bubbleSort(myArr);
        System.out.println("After: " + Arrays.toString(myArr));
        

    }

}

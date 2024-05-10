import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Try{

    static boolean isPrime(int n){
        if(n <= 1){
            return false;
        }
        for(int i=2; i<=Math.sqrt(n); i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;

    }

    static int nthPrime(int n){
        // n cannot be <= 0
        int number = 2;
        int primeCounter = 0;
        while(primeCounter < n){
            if(isPrime(number)){
                primeCounter += 1;
            }
            number += 1;
        }

        System.out.println("prime number = " + (number - 1));

        return number - 1;

    }

    static int nthOdd(int n){
        int oddCounter = 0;
        int number = 1;
        while (oddCounter < n){
            if(number % 2 != 0){
                oddCounter += 1;
            }
            number += 1;

        }
        return number - 1;
    }

    static String reverseString(String theString){
        StringBuilder sb = new StringBuilder();
        for(int i=theString.length()-1; i >=0; i--){
            sb.append(theString.charAt(i));
        }
        return sb.toString();
    }


    
    static boolean solution(int[] sequence) {
        int size = sequence.length;

        int numberOfTimesItDecreases = 0;

        for(int i=0; i <size -1; i++){
            if(sequence[i+1] <= sequence[i]){
                numberOfTimesItDecreases++;
                boolean skipNeighbor = i+2 < size && sequence[i+2] <= sequence[i];
                boolean skipBack = i-1 >=0 && sequence[i+1] <= sequence[i-1];
                if(skipNeighbor && skipBack  || numberOfTimesItDecreases >=2){return false;}
            }
        }
        return true;
    
    
    }
    
    
    
    public static void main(String[] args) {
        System.out.println("result");
        // int a[] = {1, 3, 2, 1}; // false
        // int a[] = {1, 3, 2}; // true
        // int a[] = {1, 2, 1, 2}; // false
        int a[] = {-4, -3, -2, -1}; // true
        
        System.out.println(" -> " +  solution(a));
        
        // System.out.println(" -> " +  solution(2));
        // System.out.println(" -> " +  solution(3));
        // System.out.println(" -> " +  solution(4));
        // System.out.println(" -> " +  solution(5));
        


        
    }
}

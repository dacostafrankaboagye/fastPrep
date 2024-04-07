import java.util.Arrays;

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
        int counter = 0;
        for(int i=0; i<sequence.length - 1; i++){
            if(sequence[i] < sequence[i+1]){
                continue;
            }else{
                counter++;
                if(counter >= 2){
                    return false;
                }
            }
        }
        return true;

    }
    
    public static void main(String[] args) {
        System.out.println("result");
        // int a[] = {1, 3, 2, 1};
        int a[] = {1, 3, 2};
        
        System.out.println(" -> " +  solution(a));
        // System.out.println(" -> " +  solution(2));
        // System.out.println(" -> " +  solution(3));
        // System.out.println(" -> " +  solution(4));
        // System.out.println(" -> " +  solution(5));
        


        
    }
}
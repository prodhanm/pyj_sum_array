import java.util.Scanner;

class SumArray {
    public static int sumOfArray(int arr[]) {
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            total += arr[i];
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int size;
        System.out.print("Enter the size of the array: ");
        size = inp.nextInt();
        int arr[] = new int[size];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < size; i++) {
            arr[i] = inp.nextInt();
        }
        int total = sumOfArray(arr);
        System.out.printf("The sum of the array is: %d", total);
        inp.close();
    }
}
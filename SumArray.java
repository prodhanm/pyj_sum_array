class SumArray {
    public static int sumOfArray(int arr[]) {
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            total += arr[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int total = sumOfArray(arr);
        System.out.printf("The sum of the array is: %d", total);
    }
}
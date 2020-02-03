import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.File;
import java.util.*;
public class Main {
    static int binarySearch(int[] array, int value, int low, int high) {
        int mid;
        if (high < low) {
            return -1;
        } else {
            mid = (low + high)/2;
            if (array[mid] > value) {
                return binarySearch(array, value, low, mid-1);
            } else if (array[mid] < value) {
                return binarySearch(array, value, mid+1, high);
            } else {
                return mid;
            }
        }
    }
    public static void main(String[] args) {
        File file = new File("input.in");
        Scanner sc;

        try {
            sc = new Scanner(file);
        } catch (Exception e) {
            System.out.println(e);
            sc = new Scanner(System.in);
        }
        int i, value, answer;
        int[] array = new int[10000];
        for (i=0; i<10000; i++) {
            array[i] = sc.nextInt();
        }
        try{
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.out"));
            for (i=0; i<10000; i++) {
                value = sc.nextInt();
                answer = binarySearch(array, value, 0, 9999);
                writer.write(answer + "\n");
            }
            writer.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
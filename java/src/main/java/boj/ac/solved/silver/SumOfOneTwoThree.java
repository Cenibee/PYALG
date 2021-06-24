package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SumOfOneTwoThree {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder res = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        int[] arr = new int[11];
        arr[0] = 1;
        arr[1] = 1;
        arr[2] = 2;
        for (int i = 3; i < 11; i++) {
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
        }

        for (int i = 0; i < round; i++) {
            res.append(arr[Integer.parseInt(reader.readLine())]).append('\n');
        }
        System.out.println(res);
    }

}

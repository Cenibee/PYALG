package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Atm {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        int[] arr = new int[1001];
        int max = 0;
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        while (st.hasMoreTokens()) {
            int i = Integer.parseInt(st.nextToken());
            max = Math.max(max, i);
            arr[i]++;
        }
        int sum = 0;
        int count = 0;
        for (int i = 1; i <= max; i++) {
            if (arr[i] == 0) continue;
            sum += i * arr[i] * (2 * (n - count) - arr[i] + 1) / 2;
            count += arr[i];
        }
        System.out.println(sum);

        reader.close();
    }
}

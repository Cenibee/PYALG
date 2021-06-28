package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class NAndM2 {

    static StringBuilder ans = new StringBuilder();
    static StringBuilder beforeString = new StringBuilder();
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = i + 1;

        func(0, n - 1, m);
        System.out.println(ans);

        reader.close();
    }
    private static void func(int from, int to, int count) {
        if (count == 1) {
            for (int i = from; i <= to; i++) {
                beforeString.append(arr[i]);
                ans.append(beforeString).append('\n');
                beforeString.deleteCharAt(beforeString.length() - 1);
            }
        } else {
            for (int i = from; to - i + 1 >= count; i++) {
                beforeString.append(arr[i]).append(' ');
                func(i + 1, to, count - 1);
                beforeString.delete(beforeString.length() - 2, beforeString.length());
            }
        }
    }

}

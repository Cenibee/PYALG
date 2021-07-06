package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class IntegerTriangle {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        int[] last = new int[n + 1];

        StringTokenizer st;
        for (int i = 1; i <= n; i++) {
            for (int o = i; o > 0; o--) {
                last[o] = Math.max(last[o], last[o - 1]);
            }
            st = new StringTokenizer(reader.readLine(), " ");
            for (int o = 1; o <= i; o++) {
                last[o] += Integer.parseInt(st.nextToken());
            }
        }

        int max = 0;
        for (Integer i : last)
            max = Math.max(max, i);
        System.out.println(max);

        reader.close();
    }

    public static void sol1() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        int[][] triangle = new int[n][n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(reader.readLine());
            for (int o = 0; o <= i; o++) {
                triangle[i][o] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = n - 2; i >= 0; i--) {
            for (int o = 0; o <= i; o++) {
                triangle[i][o] += Math.max(triangle[i + 1][o], triangle[i + 1][o + 1]);
            }
        }
        System.out.println(triangle[0][0]);

        reader.close();
    }
}

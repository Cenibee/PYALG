package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class FibonacciFunction {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder res = new StringBuilder();
        int t = Integer.parseInt(reader.readLine());

        int max = 0;
        int[] tArr = new int[t];
        for (int i = 0; i < t; i++) {
            int num = Integer.parseInt(reader.readLine());
            tArr[i] = num;
            max = Math.max(max, num);
        }

        int[][] fiboArr = getFiboArr(max);

        for (int i : tArr) {
            res.append(fiboArr[i][0]).append(' ').append(fiboArr[i][1]).append('\n');
        }
        System.out.println(res);

        reader.close();
    }

    private static int[][] getFiboArr(int max) {
        int[][] res = new int[max + 1][2];
        res[0][0] = 1; res[0][1] = 0;
        res[1][0] = 0; res[1][1] = 1;

        for (int i = 2; i <= max; i++) {
            res[i][0] = res[i - 1][0] + res[i - 2][0];
            res[i][1] = res[i - 1][1] + res[i - 2][1];
        }

        return res;
    }

}

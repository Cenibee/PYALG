package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BinomialCoefficient1 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int res = 1;

        int max = Math.max(k, n - k);
        int min = Math.min(k, n - k);

        for (int i = n; i > max; i--) {
            res *= i;
        }
        for (int i = 1; i <= min; i++) {
            res /= i;
        }
        System.out.println(res);

    }

}

package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Nx2Tiling {

    final static int MOD = 10007;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        int[] dp = {1, 1, 2};

        for (int i = 3; i <= n; i++) {
            dp[i % 3] = (dp[(i + 1) % 3] + dp[(i + 2) % 3]) % MOD;
        }
        System.out.println(dp[n % 3]);

        reader.close();
    }

}

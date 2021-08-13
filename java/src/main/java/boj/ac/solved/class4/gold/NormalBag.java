package boj.ac.solved.class4.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class NormalBag {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] dp = new int[k + 1];
        // (w, v)
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(reader.readLine());
            int newK = Integer.parseInt(st.nextToken());
            int newV = Integer.parseInt(st.nextToken());
            for (int w = k; w >= newK; w--) {
                dp[w] = Math.max(dp[w - newK] + newV, dp[w]);
            }
        }
        System.out.println(dp[k]);

        reader.close();
    }
}

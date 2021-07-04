package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class LongestIncreaseNums {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(reader.readLine());
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");

        int ans = 0;
        int[] checker = new int[1001];
        for (int i = 0; i < count; i++) {
            int num = Integer.parseInt(st.nextToken());
            int max = 0;
            for (int o = 1; o < num; o++) {
                max = Math.max(checker[o], max);
            }
            ans = Math.max(checker[num] = Math.max(checker[num], max + 1), ans);
        }
        System.out.println(ans);
        reader.close();
    }

}

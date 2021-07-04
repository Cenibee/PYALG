package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class RgbDistance {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = stoi(reader.readLine());
        StringTokenizer st;

        int[][] rgb = new int[2][3];

        int i = 0;
        for (; i < n; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            for (int o = 0; o < 3; o++) {
                rgb[i % 2][o] = stoi(st.nextToken()) +
                        Math.min(rgb[(i + 1) % 2][(o + 1) % 3], rgb[(i + 1) % 2][(o + 2) % 3]);
            }
        }
        int[] last = rgb[(i + 1) % 2];
        System.out.println(Math.min(last[0], Math.min(last[1], last[2])));

        reader.close();
    }

    public static int stoi(String s) {
        return Integer.parseInt(s);
    }

}

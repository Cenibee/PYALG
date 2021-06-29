package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Sticker {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        int[] upperDp = {0, 0, 0};
        int[] bottomDp = {0, 0, 0};
        for (int i = 0; i < round; i++) {
            int col = Integer.parseInt(reader.readLine());
            int[] upper = getArray(reader, col);
            int[] bottom = getArray(reader, col);
            Arrays.fill(upperDp, 0);
            Arrays.fill(bottomDp, 0);

            int o = 0;
            for (; o < col; o++) {
                int far = Math.max(upperDp[(o + 1) % 3], bottomDp[(o + 1) % 3]);
                upperDp[o % 3] = Math.max(far, bottomDp[(o + 2) % 3]) + upper[o];
                bottomDp[o % 3] = Math.max(far, upperDp[(o + 2) % 3]) + bottom[o];
            }
            ans.append(Math.max(upperDp[(o - 1) % 3], bottomDp[(o - 1) % 3])).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

    private static int[] getArray(BufferedReader reader, int col) throws IOException {
        int[] upper = new int[col];
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        for (int o = 0; o < col; o++)
            upper[o] = Integer.parseInt(st.nextToken());
        return upper;
    }
}

package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Z {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int result = 0;
        int edgeLength = 1;
        int constant = 1;
        for (int i = 0; i < n - 1; i++) {
            edgeLength *= 2;
            constant *= 4;
        }
        for (; edgeLength > 0; edgeLength /= 2) {
            if (r >= edgeLength) {
                result += 2 * constant;
                r -= edgeLength;
            }
            if (c >= edgeLength) {
                result += constant;
                c -= edgeLength;
            }
            constant /= 4;
        }
        System.out.println(result);

        reader.close();
    }

}

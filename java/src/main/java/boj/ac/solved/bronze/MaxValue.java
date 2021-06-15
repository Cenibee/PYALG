package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MaxValue {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int res = -1;
        int max = 0;
        for (int i = 1; i <= 9; i++) {
            int comp = Integer.parseInt(br.readLine());
            if (comp > max) {
                res = i;
                max = comp;
            }
        }
        System.out.println(max + "\n" + res);
    }

}

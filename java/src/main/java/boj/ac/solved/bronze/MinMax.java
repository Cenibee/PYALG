package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MinMax {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        reader.readLine();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        String[] nums = reader.readLine().split(" ");

        for (String s : nums) {
            int cur = Integer.parseInt(s);
            min = Math.min(min, cur);
            max = Math.max(max, cur);
        }
        System.out.println(String.join(" ", Integer.toString(min), Integer.toString(max)));
    }

}

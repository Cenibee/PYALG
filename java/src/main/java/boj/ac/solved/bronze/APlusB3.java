package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class APlusB3 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            String[] split = reader.readLine().split(" ");
            System.out.println(Integer.parseInt(split[0]) + Integer.parseInt(split[1]));
        }
    }

}

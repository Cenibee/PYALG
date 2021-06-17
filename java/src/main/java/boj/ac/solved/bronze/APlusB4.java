package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class APlusB4 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        reader.lines().forEach(s -> {
            String[] split = s.split(" ");
            System.out.println(Integer.parseInt(split[0]) + Integer.parseInt(split[1]));
        });
    }

}

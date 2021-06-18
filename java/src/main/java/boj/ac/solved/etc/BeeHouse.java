package boj.ac.solved.etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BeeHouse {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int target = Integer.parseInt(reader.readLine());
        if (target-- == 1) {
            System.out.println(1);
            return;
        }
        for (int i = 1; ; i++) {
            target = target - i * 6;
            if (target <= 0) {
                System.out.println(i + 1);
                return;
            }
        }
    }
}

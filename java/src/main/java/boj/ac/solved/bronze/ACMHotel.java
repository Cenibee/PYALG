package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ACMHotel {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            String[] split = reader.readLine().split(" ");
            int h = Integer.parseInt(split[0]);
            int custom = Integer.parseInt(split[2]) - 1;
            int floor = custom % h + 1;
            int num = custom / h + 1;
            System.out.println(String.join(num > 9 ? "" : "0", Integer.toString(floor), Integer.toString(num)));
        }
    }

}

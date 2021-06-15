package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class RepeatString {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            String[] split = reader.readLine().split(" ");
            int repeat = Integer.parseInt(split[0]);
            StringBuffer sb = new StringBuffer();
            for (int c = 0; c < split[1].length(); c++) {
                sb.append(String.valueOf(split[1].charAt(c)).repeat(repeat));
            }
            System.out.println(sb);
        }

    }

}

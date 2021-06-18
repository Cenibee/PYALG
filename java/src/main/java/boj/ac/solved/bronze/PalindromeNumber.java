package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PalindromeNumber {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String num = reader.readLine();
            if (num.equals("0")) break;

            String res = "yes";
            for (int i = 0; i < num.length() / 2; i++) {
                if (num.charAt(i) != num.charAt(num.length() - i - 1)) {
                    res = "no";
                    break;
                }
            }
            System.out.println(res);
        }
    }

}

package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Parenthesis {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();

        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            int checker = 0;
            String str = reader.readLine();
            for (int o = 0; o < str.length(); o++) {
                if (str.charAt(o) == '(') {
                    checker++;
                } else if (str.charAt(o) == ')') {
                    checker--;
                    if (checker < 0) {
                        break;
                    }
                }
            }
            result.append(checker == 0 ? "YES\n" : "NO\n");
        }
        System.out.println(result);
        reader.close();
    }

}

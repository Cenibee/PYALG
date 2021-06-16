package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class OXQuiz {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int round = Integer.parseInt(reader.readLine());

        for (int r = 0; r < round; r++) {
            String res = reader.readLine();
            int score = 0;
            int stack = 1;
            for (int i = 0; i < res.length(); i++) {
                if (res.charAt(i) == 'O') {
                    score+=stack++;
                } else {
                    stack = 1;
                }
            }
            System.out.println(score);
        }
    }

}

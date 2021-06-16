package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MusicScale {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String read = reader.readLine();
        if ("1 2 3 4 5 6 7 8".equals(read)) {
            System.out.println("ascending");
        } else if ("8 7 6 5 4 3 2 1".equals(read)) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }

}

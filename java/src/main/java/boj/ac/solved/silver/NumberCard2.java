package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class NumberCard2 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();
        reader.readLine();

        Map<String, Integer> numCount = new HashMap<>();
        StringTokenizer numTokens = new StringTokenizer(reader.readLine(), " ");
        while (numTokens.hasMoreTokens()) {
            String token = numTokens.nextToken();
            numCount.put(token, numCount.getOrDefault(token, 0) + 1);
        }
        reader.readLine();

        numTokens = new StringTokenizer(reader.readLine(), " ");
        while (numTokens.hasMoreTokens()) {
            result.append(numCount.getOrDefault(numTokens.nextToken(), 0)).append(' ');
        }
        System.out.println(result);
        reader.close();
    }

}

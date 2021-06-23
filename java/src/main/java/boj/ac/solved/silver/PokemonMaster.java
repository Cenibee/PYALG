package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class PokemonMaster {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();

        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] numToPoke = new String[n + 1];
        Map<String, Integer> pokeToNum = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            String pokemon = reader.readLine();
            numToPoke[i] = pokemon;
            pokeToNum.put(pokemon, i);
        }

        for (int i = 0; i < m; i++) {
            String quiz = reader.readLine();
            if ('0' <= quiz.charAt(0) && quiz.charAt(0) <= '9') {
                result.append(numToPoke[Integer.parseInt(quiz)]).append('\n');
            } else {
                result.append(pokeToNum.get(quiz)).append('\n');
            }
        }
        System.out.println(result);

        reader.close();
    }

}

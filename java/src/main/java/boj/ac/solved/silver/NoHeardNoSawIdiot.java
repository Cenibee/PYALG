package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Set;

public class NoHeardNoSawIdiot {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder("\n");

        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Set<String> noHeard = new HashSet<>();
        for (int i = 0; i < n; i++) {
            noHeard.add(reader.readLine());
        }
        List<String> noHeardNoSaw = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String noSaw = reader.readLine();
            if (noHeard.contains(noSaw)) {
                noHeardNoSaw.add(noSaw);
            }
        }
        noHeardNoSaw.sort(String::compareTo);
        System.out.println(noHeardNoSaw.size());
        System.out.println(String.join("\n", noHeardNoSaw));

        reader.close();
    }
}

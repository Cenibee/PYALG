package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class SortPosition {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        List<List<Integer>> positions = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            positions.add(List.of(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        positions.sort((o1, o2) -> {
            if (o1.get(0).equals(o2.get(0))) {
                return o1.get(1).compareTo(o2.get(1));
            }
            return o1.get(0).compareTo(o2.get(0));
        });

        StringBuilder sb = new StringBuilder();
        for (List<Integer> position : positions) {
            sb.append(position.get(0)).append(' ').append(position.get(1)).append('\n');
        }
        System.out.println(sb);
    }

}

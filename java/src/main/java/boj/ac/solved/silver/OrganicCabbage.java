package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class OrganicCabbage {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder res = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            st.nextToken();st.nextToken();
            res.append(startRound(reader, Integer.parseInt(st.nextToken()))).append('\n');
        }
        System.out.println(res);

        reader.close();
    }

    private static int startRound(BufferedReader reader, int cabbageCount) throws IOException {
        StringTokenizer st;
        Set<List<Integer>> cabbages = new HashSet<>();
        for (int o = 0; o < cabbageCount; o++) {
            st = new StringTokenizer(reader.readLine(), " ");
            cabbages.add(List.of(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        int count = 0;
        while (cabbages.size() != 0) {
            count++;
            dfs(cabbages, cabbages.iterator().next());
        }
        return count;
    }

    final static int[] row_ = {0, 0, 1, -1};
    final static int[] col_ = {1, -1, 0, 0};
    private static void dfs(Set<List<Integer>> cabbages, List<Integer> fromCabbage) {
        if (!cabbages.remove(fromCabbage)) return;

        for (int i = 0; i < 4; i++) {
            dfs(cabbages, List.of(fromCabbage.get(0) + row_[i], fromCabbage.get(1) + col_[i]));
        }
    }
}

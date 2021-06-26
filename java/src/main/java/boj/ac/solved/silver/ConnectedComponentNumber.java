package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Set;

public class ConnectedComponentNumber {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int vertexes = Integer.parseInt(st.nextToken());
        int edges = Integer.parseInt(st.nextToken());

        Map<Integer, Set<Integer>> edgeMap = new HashMap<>();
        for (int i = 1; i <= vertexes; i++) {
            edgeMap.put(i, new HashSet<>());
        }

        for (int i = 0; i < edges; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edgeMap.get(a).add(b);
            edgeMap.get(b).add(a);
        }

        int result = 0;
        Stack<Integer> dfs = new Stack<>();
        while (edgeMap.size() != 0) {
            result++;
            int one = edgeMap.keySet().iterator().next();
            dfs.addAll(edgeMap.remove(one));
            while (dfs.size() != 0) {
                Set<Integer> search = edgeMap.remove(dfs.pop());
                if (search == null) continue;
                dfs.addAll(search);
            }
        }
        System.out.println(result);

        reader.close();
    }

}

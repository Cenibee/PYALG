package programmers.level3;

import java.util.*;

public class FarthestNode {
    public int solution(int n, int[][] edge) {
        Map<Integer, List<Integer>> edges = new HashMap<>();
        for (int i = 1; i <= n; i++) edges.put(i, new LinkedList<>());

        for (int[] e : edge) {
            edges.get(e[0]).add(e[1]);
            edges.get(e[1]).add(e[0]);
        }

        LinkedList<Integer> q = new LinkedList<>();
        q.add(1);

        int limit = 1;
        while (!q.isEmpty()) {
            Set<Integer> next = new HashSet<>();
            limit = q.size();
            for (int i = 0; i < limit; i++)
                next.addAll(edges.remove(q.pollFirst()));
            for (int i : next)
                if (edges.containsKey(i))
                    q.add(i);
        }

        return limit;
    }
}

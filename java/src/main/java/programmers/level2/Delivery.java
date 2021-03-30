package programmers.level2;

import java.util.*;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12978
 */
public class Delivery {
    public int solution(int N, int[][] road, int K) {
        Map<Integer, Map<Integer, Integer>> dist = new HashMap<>();
        for (int i = 1; i <= N; i++) dist.put(i, new HashMap<>());
        for (int[] r : road) {
            if (dist.get(r[0]).getOrDefault(r[1], K + 1) <= r[2]) continue;
            dist.get(r[0]).put(r[1], r[2]);
            dist.get(r[1]).put(r[0], r[2]);
        }

        LinkedList<Integer> q = new LinkedList<>();
        q.add(1);
        int[] visited = new int[N + 1];
        Arrays.fill(visited, K + 1);
        visited[1] = 0;

        while (q.size() > 0) {
            int pos = q.pollFirst();
            for (Map.Entry<Integer, Integer> e : dist.get(pos).entrySet()) {
                int d = visited[pos] + e.getValue();
                if (d >= Math.min(visited[e.getKey()], K + 1)) continue;
                visited[e.getKey()] = d;
                q.add(e.getKey());
            }
        }
        int answer = 0;
        for (int i : visited) if (i < K + 1) answer++;
        return answer;
    }
}

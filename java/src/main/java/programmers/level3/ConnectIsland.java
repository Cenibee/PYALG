package programmers.level3;

import java.util.*;

public class ConnectIsland {
    public int solution(int n, int[][] costs) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int i = 0; i < n; i++) map.put(i, new ArrayList<>());
        for (int[] cost : costs) {
            map.get(cost[0]).add(new int[]{cost[1], cost[2]});
            map.get(cost[1]).add(new int[]{cost[0], cost[2]});
        }

        PriorityQueue<int[]> q = new PriorityQueue<>(
                Comparator.comparingInt((int[] a) -> a[1])
        );
        // 시작점을 가져온다.
        q.addAll(map.remove(0));

        int answer = 0;
        // map 이 소모될 때 까지
        while (!map.isEmpty() && !q.isEmpty()) {
            // 가용한 다리중 가장 싼거 가져오고
            int[] min = q.poll();
            answer += Optional.ofNullable(map.remove(min[0]))
                    .flatMap(ints -> {
                        q.addAll(ints);
                        return Optional.of(min[1]);
                    }).orElse(0);
        }
        return answer;
    }
}

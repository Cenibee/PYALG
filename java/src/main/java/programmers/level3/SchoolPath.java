package programmers.level3;

import java.util.*;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/42898
 */
public class SchoolPath {
    private final int MOD = 1000000007;

    public int solution(int m, int n, int[][] puddles) {
        Map<Integer, Set<Integer>> puddleMap = new HashMap<>();
        for (int[] puddle : puddles) {
            if (!puddleMap.containsKey(puddle[0]))
                puddleMap.put(puddle[0], new HashSet<>());
            puddleMap.get(puddle[0]).add(puddle[1]);
        }

        int[] line = new int[n + 1];
        Arrays.fill(line, 0);
        line[0] = 1;

        for (int i = 1; i <=m; i++) {
            if (puddleMap.containsKey(i))
                for (Integer trap : puddleMap.remove(i))
                    line[trap] = -1;
            for (int o = 1; o <= n; o++)
                line[o] = line[o] == -1 ? 0 :
                        (line[o] + line[o - 1]) % MOD;
            line[0] = 0;
        }
        return line[n];
    }
}

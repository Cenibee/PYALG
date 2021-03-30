package programmers.level2;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/1844?language=java
 */
public class GameMapShortestPath {
    public int solution(int[][] maps) {
        int m = maps.length - 1;
        int n = maps[0].length - 1;

        int[][] newmaps = new int[maps.length + 2][maps[0].length + 2];
        Arrays.fill(newmaps[0], 0);
        Arrays.fill(newmaps[newmaps.length - 1], 0);
        for (int i = 0; i < maps.length; i++)
            for (int o = 0; o < maps[0].length; o++)
                newmaps[i + 1][o + 1] = maps[i][o];
        for (int[] newmap : newmaps) System.out.println(Arrays.toString(newmap));

        // 상하 좌우
        int[] x_ = {1, -1, 0, 0};
        int[] y_ = {0, 0, 1, -1};

        LinkedList<List<Integer>> queue = new LinkedList<>();
        queue.add(List.of(0, 0));

        int cur = 0;
        while (queue.size() > 0) {
            cur++;
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                List<Integer> xy = queue.pollFirst();
                maps[xy.get(1)][xy.get(0)] = cur != 1 ? cur : 0;
                if (xy.get(0) == n && xy.get(1) == m)
                    return maps[xy.get(1)][xy.get(0)];
                for (int o = 0; o < 4; o++) {
                    int next_x = x_[o] + xy.get(0);
                    int next_y = y_[o] + xy.get(1);
                    if (next_x >= 0 && next_x < maps[0].length
                            && next_y >= 0 && next_y < maps.length &&
                            maps[next_y][next_x] == 1) {
                        maps[next_y][next_x] = 0;
                        queue.add(List.of(next_x, next_y));
                    }

                }
            }
        }
        return -1;
    }
}
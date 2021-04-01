package programmers.level3;

import java.util.Arrays;
import java.util.Comparator;

public class RoadCamera {
    public int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparingInt((int[] a) -> a[0]));

        int answer = 0;
        int minExit = -30000;
        for (int[] route : routes) {
            // 현재 시작이 가장 먼저 끝난 경로 이후면 ++
            if (minExit < route[0]) {
                answer++;
                minExit = route[1];
            } else if (route[1] < minExit)
                minExit = route[1];
        }

        return answer;
    }

    public int optimize(int [][] routes) {
        Arrays.sort(routes, Comparator.comparingInt((int[] a) -> a[1]));

        int answer = 0;
        int minExit = -30000;
        for (int[] route : routes) {
            if (minExit < route[0]) {
                answer++;
                minExit = route[1];
            }
        }

        return answer;
    }
}

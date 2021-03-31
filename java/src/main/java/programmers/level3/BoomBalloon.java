package programmers.level3;

import java.util.*;

public class BoomBalloon {
    public int solution(int[] a) {
        int minIdx = 0;
        // 최소값 찾기
        for (int i = 1; i < a.length; i++)
            if (a[minIdx] > a[i]) minIdx = i;
        return subFunction(a, 0, minIdx, true) + subFunction(a, minIdx, a.length, false);
    }

    private int subFunction(int[] a, int from, int to, boolean bigger) {
        int answer = 0;
        LinkedList<List<Integer>> q = new LinkedList<>();
        for (int i = from; i < to; i++) q.add(List.of(i, a[i]));
        q.sort(Comparator.comparingInt((List<Integer> arr) -> arr.get(1)));
        int subMinIdx = bigger ? to : from;
        while (!q.isEmpty()) {
            Integer idx = q.pollFirst().get(0);
            if (subMinIdx > idx == bigger) {
                answer++;
                subMinIdx = idx;
            }
        }
        return answer;
    }

    public int optimize(int[] a) {
        int leftMin = Integer.MIN_VALUE;
        int rightMin = Integer.MIN_VALUE;

        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < a.length; i++) {
            leftMin = Math.min(leftMin, a[i]);
            set.add(leftMin);
            rightMin = Math.min(rightMin, a[a.length - i - 1]);
            set.add(rightMin);
        }
        return set.size();
    }
}

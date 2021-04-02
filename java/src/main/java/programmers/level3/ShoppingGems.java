package programmers.level3;

import java.util.*;

public class ShoppingGems {
    public int[] solution(String[] gems) {
        Set<String> gemSet = new HashSet<>();
        Collections.addAll(gemSet, gems);
        Map<String, Integer> map = new HashMap<>();

        // left 다음에 빼야할 위치 / right 다음에 더할 보석 위치
        int left = 0;
        int right = 0;
        // 시작, 끝
        int[] range = new int[]{1, gems.length};

        while (right < gems.length) {
            // 다음 보석을 추가하고
            map.put(gems[right], map.getOrDefault(gems[right++], 0) + 1);

            // 모든 보석이 포함된 상태가 되었을 때부터
            if (map.size() == gemSet.size()) {
                // 왼쪽에서부터 중복된 보석들 제거
                int leftCnt;
                while ((leftCnt = map.get(gems[left])) > 1)
                    map.put(gems[left++], leftCnt - 1);
                if (range[1] - range[0] >  right - (left + 1)) {
                    range[0] = left + 1;
                    range[1] = right;
                }
            }
        }

        return range;
    }
}

package programmers.level2;

import java.util.HashSet;
import java.util.Set;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12981
 */
public class ConnectTheEnd {
    public int[] solution(int n, String[] words) {
        Set<String> set = new HashSet<>();
        char last = words[0].charAt(0);
        for (int i = 0; i < words.length; i++) {
            if (last != words[i].charAt(0) || !set.add(words[i]))
                return new int[]{i % n + 1, i / n + 1};
            last = words[i].charAt(words[i].length() - 1);
        }
        return new int[]{0, 0};
    }
}
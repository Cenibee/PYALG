package programmers.level2;

import java.util.Arrays;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12939
 */
public class MaxMinValue {
    public String solutionStream(String s) {
        int[] arr = Arrays.stream(s.split(" "))
                .mapToInt(str -> Integer.valueOf(str))
                .sorted()
                .toArray();
        return new StringBuilder()
                .append(arr[0])
                .append(' ')
                .append(arr[arr.length - 1])
                .toString();
    }

    public String solutionNonStream(String s) {
        String[] strs = s.split(" ");
        int min, max;
        min = max = Integer.parseInt(strs[0]);

        for (int i = 1; i < strs.length; i++) {
            int n = Integer.parseInt(strs[i]);
            max = Math.max(max, n);
            min = Math.min(min, n);
        }
        return new StringBuilder()
                .append(min)
                .append(' ')
                .append(max)
                .toString();
    }
}

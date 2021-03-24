package programmers.level2;

import java.util.stream.IntStream;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/42747#
 */
public class HIndex {
    public int solution(int[] citations) {
        Integer[] sorted = IntStream.of(citations)
                .boxed()
                .sorted((Integer a, Integer b) -> b - a)
                .toArray(Integer[]::new);
        for (int i = 0; i < sorted.length; i++)
            if (sorted[i] < i + 1)
                return i;
        return citations.length;
    }
}

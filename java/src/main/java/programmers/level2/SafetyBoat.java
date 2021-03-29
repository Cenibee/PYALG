package programmers.level2;

import java.util.Arrays;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/42885
 */
public class SafetyBoat {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0;
        int right = people.length - 1;
        int boats = 0;

            while (left <= right) {
            int w = people[right--];
            boats++;
            if (left <= right && w + people[left] <= limit)
                left++;
        }
        return boats;
    }
}

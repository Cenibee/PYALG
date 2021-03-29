package programmers.level2;

import java.util.Arrays;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12953#
 */
public class MinimumLCM {
    public int solution(int[] arr) {
        int[] primes = 	{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
        int answer = 1;
        for (int prime : primes) {
            int max = prime;
            for (int i : arr) while (i % max == 0) max *= prime;
            answer = answer * (max / prime);
        }
        return answer;
    }
}

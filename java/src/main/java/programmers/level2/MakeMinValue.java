package programmers.level2;

import java.util.Arrays;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12941
 */
public class MakeMinValue {
    public int solution(int []A, int []B) {
        Arrays.sort(A);
        Arrays.sort(B);
        int answer = 0;
        for (int i = 0; i < A.length; i++)
            answer += A[i] * B[A.length - i - 1];
        return answer;
    }
}

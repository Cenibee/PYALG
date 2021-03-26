package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12945#
 */
public class Fibonacci {
    static final int DIVIDE = 1234567;
    public int solution(int n) {
        int[] arr = {1, 1};
        int p = 0;
        int curResult = 2;
        for (;curResult != n; curResult++)
            arr[p = (p + 1) % 2] = (arr[0] % DIVIDE + arr[1] % DIVIDE) % DIVIDE;
        return arr[p];
    }
}

package programmers.level3;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12900
 */
public class Nx2Tiling {
    private static final int DIV = 1000000007;
    public int solution(int n) {
        int[] arr = new int[]{0, 1, 2};
        if (n == 1 || n == 2) return n;
        int i = 3;
        for (; i <= n; i++)
            arr[i % 3] = (arr[(i - 1) % 3] % DIV + arr[(i - 2) % 3]) % DIV;
        return arr[(i - 1) % 3];
    }
}

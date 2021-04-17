package programmers.level3;

public class JumpAway {
    public long solution(int n) {
        int[] step = {2, 1};
        for (int i = 3; i <= n; i++)
            step[i % 2] = (step[i % 2] + step[(i + 1) % 2]) % 1234567;
        return step[n % 2];
    }
}

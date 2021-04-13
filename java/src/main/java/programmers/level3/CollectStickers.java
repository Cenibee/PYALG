package programmers.level3;

public class CollectStickers {
    public int solution(int sticker[]) {
        if (sticker.length == 1) return sticker[0];
        else if (sticker.length == 2) return Math.max(sticker[0], sticker[1]);

        int answer = 0;
        for (int i = 0; i < 3; i++) {
            // sticker[i]를 뜯었을 때 최대값을 DP로 구한다.
            answer = Math.max(
                    answer,
                    sticker[i] + subDp(sticker, sticker.length,
                            (i + 2) % sticker.length));
        }
        return answer;
    }

    private int subDp(int[] arr, int len, int from) {
        int[] dp = new int[]{0, 0, 0, 0};

        for (int i = 0; i < len - 3; i++) {
            dp[i % 4] = Math.max(dp[(i + 1) % 4] + arr[from], dp[(i + 2) % 4] + arr[from]);
            from = (from + 1) % len;
        }

        return Math.max(dp[0], Math.max(dp[1], Math.max(dp[2], dp[3])));
    }
}

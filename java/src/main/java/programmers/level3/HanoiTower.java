package programmers.level3;

public class HanoiTower {
    // from 에서 to 로 num 개 이동시키는 방법 나열
    private int move(
            int[][] arr, int arrFrom, int num,
            int from, int to, int another
    ) {
        if (num == 0) return arrFrom;
        arrFrom = move(arr, arrFrom, num - 1, from, another, to);
        arr[arrFrom++] = new int[]{from, to};
        arrFrom = move(arr, arrFrom, num - 1, another, to, from);
        return arrFrom;

    }

    public int[][] solution(int n) {
        int[][] answer = new int[(int)Math.pow(2, n) - 1][2];
        move(answer, 0, n, 1, 3, 2);
        return answer;
    }
}

package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12949
 */
public class MetrixMult {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        for (int i = 0; i < arr1.length; i++) {
            for (int o = 0; o < arr2[0].length; o++) {
                answer[i][o] = 0;
                for (int p = 0; p < arr2.length; p++)
                    answer[i][o] += arr1[i][p] * arr2[p][o];
            }
        }
        return answer;
    }
}

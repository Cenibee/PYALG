package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12905#
 */
public class FindBiggestSquare {
    public int solution(int [][]board)
    {
        int max = 0;
        for (int i = 0; i < board.length; i++) {
            for (int o = 0; o < board[i].length; o++) {
                if (board[i][o] == 0) continue;
                int width = 0;
                int upper = i > 0 ? board[i - 1][o] : 0;
                int left = o > 0 ? board[i][o - 1] : 0;
                if (upper == left) {
                    if (upper == 0 || board[i - 1][o - 1] >= upper)
                        width = upper + 1;
                    else
                        width = upper;
                }
                else
                    width = Math.min(left, upper) + 1;
                board[i][o] = width;
                max = Math.max(max, width);
            }
        }
        return max * max;
    }
}

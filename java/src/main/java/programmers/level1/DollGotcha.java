package programmers.level1;

import java.util.Stack;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/64061
 */
public class DollGotcha {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer>[] myBoard = new Stack[board[0].length];
        for (int i = 0; i < myBoard.length; i++) myBoard[i] = new Stack<>();

        for (int i = 0; i < board[0].length; i++) {
            for (int o = board.length - 1; o >= 0; o--) {
                if (board[o][i] == 0) break;
                myBoard[i].push(board[o][i]);
            }
        }

        int answer = 0;
        Stack<Integer> basket = new Stack<>();
        for (int from : moves) {
            if (myBoard[from - 1].isEmpty()) continue;
            Integer doll = myBoard[from - 1].pop();
            if (basket.isEmpty() || !basket.peek().equals(doll))
                basket.push(doll);
            else {
                basket.pop();
                answer += 2;
            }
        }

        return answer;
    }
}

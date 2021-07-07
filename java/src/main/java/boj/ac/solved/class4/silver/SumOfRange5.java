package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SumOfRange5 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            for (int o = 1; o <= n; o++) {
                board[i][o] = board[i][o - 1] + board[i - 1][o] - board[i - 1][o - 1] + Integer.parseInt(st.nextToken());
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int startX = Integer.parseInt(st.nextToken());
            int startY = Integer.parseInt(st.nextToken());
            int endX = Integer.parseInt(st.nextToken());
            int endY = Integer.parseInt(st.nextToken());
            ans.append(board[endX][endY] - board[startX - 1][endY] - board[endX][startY - 1] + board[startX - 1][startY - 1]).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

}

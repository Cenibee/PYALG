package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ColorPaper {

    private static boolean[][] board;
    private static int[] res;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        // 흰색 false / 파란색 true
        board = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String line = reader.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = line.charAt(j * 2) == '1';
            }
        }

        res = new int[]{0, 0};
        int last = subFunc(0, 0, n);
        if (last != 2) {
            res[last]++;
        }

        System.out.println(res[0] + "\n" + res[1]);

        reader.close();
    }

    // 전체가 흰색이면 0, 전체가 파랑이면 1, 집계됐으면 2
    private static int subFunc(int row, int col, int length) {
        if (length == 1) return board[row][col] ? 1 : 0;

        int halfLen = length / 2;
        int[] tempRes = {0, 0, 0};

        tempRes[subFunc(row, col, halfLen)]++;
        tempRes[subFunc(row + halfLen, col, halfLen)]++;
        tempRes[subFunc(row, col + halfLen, halfLen)]++;
        tempRes[subFunc(row + halfLen, col + halfLen, halfLen)]++;

        if (tempRes[0] == 4) {
            return 0;
        } else if (tempRes[1] == 4) {
            return 1;
        } else {
            res[0] += tempRes[0];
            res[1] += tempRes[1];
            return 2;
        }
    }

}

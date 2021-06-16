package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class RecolorChessBoard {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        // 첫 째줄 입력
        String[] firstLine = reader.readLine().split(" ");
        int row = Integer.parseInt(firstLine[0]);
        int col = Integer.parseInt(firstLine[1]);

        // 전체 판 초기화
        List<List<Boolean>> totalBoard = new ArrayList<>();
        for (int i = 0; i < row; i++) {
            String s = reader.readLine();
            ArrayList<Boolean> list = new ArrayList<>();
            for (int o = 0; o < s.length(); o++)
                list.add(s.charAt(o) == 'B');
            totalBoard.add(list);
        }

        // evenW, evenB, oddW, oddB - 접두사는 col + row 합의 짝/홀 여부
        int[] score = {0, 0, 0, 0};

        int next_col = 8;
        int next_row = 8;

        for (int i = 0; i < next_col; i++)
            for (int o = 0; o < next_row; o++)
                score[((i + o) % 2) * 2 + (totalBoard.get(o).get(i) ? 1 : 0)]++;

        int res = getMin(score);

        for (int i = next_row; i <= row; i++) {
            int[] roundScore = score.clone();
            for (int o = next_col; o < col; o++) {
                for (int p = i - 8; p < i; p++) {
                    roundScore[((p + o) % 2) * 2 + (totalBoard.get(p).get(o) ? 1 : 0)]++;
                    roundScore[((p + o - 8) % 2) * 2 + (totalBoard.get(p).get(o - 8) ? 1 : 0)]--;
                }
                res = Math.min(res, getMin(roundScore));
            }

            if (row == i)
                break;

            for (int o = 0; o < 8; o++) {
                score[((i + o) % 2) * 2 + (totalBoard.get(i).get(o) ? 1 : 0)]++;
                score[((i - 8 + o) % 2) * 2 + (totalBoard.get(i - 8).get(o) ? 1 : 0)]--;
            }
            res = Math.min(res, getMin(score));
        }

        System.out.println(res);
    }

    private static int getMin(int[] roundScore) {
        return Math.min(roundScore[0] + roundScore[3], roundScore[1] + roundScore[2]);
    }

}

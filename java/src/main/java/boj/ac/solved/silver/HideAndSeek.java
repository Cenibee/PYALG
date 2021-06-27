package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class HideAndSeek {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int s = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        if (s >= d) {
            System.out.println(s - d);
            return;
        }

        int round = -1;
        boolean end = false;
        List<Integer> list = List.of(s);
        boolean[] checker = new boolean[100001];
        do {
            round++;
            List<Integer> tempList = new ArrayList<>();
            for (Integer check : list) {
                if (check == d) {
                    end = true;
                    break;
                }
                checker[check] = true;
                if (check > 0 && !checker[check - 1])
                    tempList.add(check - 1);
                if (check < 100000 && !checker[check + 1])
                    tempList.add(check + 1);
                if (check <= 50000 && !checker[check * 2])
                    tempList.add(check * 2);
            }
            list = tempList;
        } while (!end);
        System.out.println(round);

        reader.close();
    }

}

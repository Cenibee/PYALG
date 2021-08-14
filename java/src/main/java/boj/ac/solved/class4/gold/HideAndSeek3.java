package boj.ac.solved.class4.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HideAndSeek3 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int subin = Integer.parseInt(st.nextToken());
        int sister = Integer.parseInt(st.nextToken());

        if (subin >= sister) {
            System.out.println(subin - sister);
            reader.close();
            return;
        }

        int[] line = new int[100001];
        for (int i = 1; subin - i >= 0; i++) line[subin - i] = i;
        int max = sister + 1;
        for (int i = subin + 1; i <= 100000 && i <= max; i++) {
            if (i % 2 == 0) {
                line[i] = Math.min(line[i - 1] + 1, line[i / 2]);
                if (line[i] + 1 < line[i - 1]) line[i - 1] = line[i] + 1;
            } else {
                line[i] = line[i - 1] + 1;
            }
        }
        System.out.println(line[sister]);
        reader.close();
    }

}

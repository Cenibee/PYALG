package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class AssignRoom {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int count = strToNum(reader.readLine());

        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            list.add(new int[]{strToNum(st.nextToken()), strToNum(st.nextToken())});
        }
        list.sort((int[] arr1, int[] arr2) -> {
            if (arr1[1] == arr2[1]) {
                return arr1[0] - arr2[0];
            } else {
                return arr1[1] - arr2[1];
            }
        });

        int result = 0;
        int lastFinish = 0;
        for (int[] timeRange : list) {
            if (lastFinish <= timeRange[0]) {
                result++;
                lastFinish = timeRange[1];
            }
        }
        System.out.println(result);

        reader.close();
    }

    private static int strToNum(String s) {
        return Integer.parseInt(s);
    }

}

package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class NAndM5 {

    static StringBuilder ans = new StringBuilder();
    static StringBuilder beforeString = new StringBuilder();
    static int[] arr;
    static Set<Integer> remainIndexes = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(reader.readLine(), " ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            remainIndexes.add(i);
        }
        Arrays.sort(arr);

        func(m);
        System.out.println(ans);

        reader.close();
    }
    private static void func(int count) {
        if (count == 1) {
            for (int i : remainIndexes) {
                beforeString.append(arr[i]);
                ans.append(beforeString).append('\n');
                beforeString.delete(beforeString.lastIndexOf(" ") + 1, beforeString.length());
            }
        } else {
            List<Integer> temp = List.copyOf(remainIndexes);
            for (int i : temp) {
                remainIndexes.remove(i);
                beforeString.append(arr[i]).append(' ');
                func(count - 1);
                beforeString.delete(beforeString.lastIndexOf(" ", beforeString.length() - 2) + 1, beforeString.length());
                remainIndexes.add(i);
            }
        }
    }

}

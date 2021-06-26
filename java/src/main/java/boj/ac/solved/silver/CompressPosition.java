package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Set;

public class CompressPosition {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int num = Integer.parseInt(br.readLine());

        int[] input = new int[num];
        TreeSet<Integer> tree = new TreeSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < num; i++) {
            tree.add(input[i] = Integer.parseInt(st.nextToken()));
        }
        HashMap<Integer, Integer> compressMap = new HashMap<>();
        for (int i = 0; tree.size() != 0; i++) {
            int min = tree.first();
            compressMap.put(min, i);
            tree.remove(min);
        }
        for (int elem : input) {
            ans.append(compressMap.get(elem)).append(' ');
        }
        System.out.println(ans);

        br.close();
    }


}

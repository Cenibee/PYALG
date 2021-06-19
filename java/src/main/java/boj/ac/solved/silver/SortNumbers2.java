package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class SortNumbers2 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(reader.readLine());
        List<Integer> nums = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(reader.readLine()));
        }
//        nums.stream().sorted().forEach(i -> sb.append(i).append('\n'));
        nums.sort(Integer::compare);
        for (Integer num : nums) {
            sb.append(num).append('\n');
        }

        System.out.println(sb);
    }

}

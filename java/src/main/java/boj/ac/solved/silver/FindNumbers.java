package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Set;

public class FindNumbers {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        reader.readLine();

        // 정렬된 첫 번째 리스트 생성
        Set<Integer> nums = new HashSet<>();
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        while (st.hasMoreElements()) {
            nums.add(Integer.parseInt(st.nextToken()));
        }

        reader.readLine();
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(reader.readLine(), " ");
        while (st.hasMoreElements()) {
            sb.append(nums.contains(Integer.parseInt(st.nextToken())) ? 1 : 0).append('\n');
        }
        System.out.println(sb);
    }

}

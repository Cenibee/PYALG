package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BlackJack {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        // 상수 세팅
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 정렬된 배열 세팅
        st = new StringTokenizer(reader.readLine(), " ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int max = 0;
        for (int i = 0; i < n - 2; i++) {

            // i 번째 값이 포함되는 경우, m보다 작거나 같은 가장 가까운 합을 구한다.
            int target = m - nums[i];
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum < target) {
                    max = Math.max(max, sum + nums[i]);
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    System.out.println(m);
                    return;
                }
            }
        }
        System.out.println(max);
    }

}

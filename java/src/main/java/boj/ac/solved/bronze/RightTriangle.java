package boj.ac.solved.bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class RightTriangle {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String s;
        while (!(s = reader.readLine()).startsWith("0")) {
            if (s.startsWith("0")) return;
            String[] split = s.split(" ");
            int[] nums = {pow(split[0]), pow(split[1]), pow(split[2])};
            if (nums[0] < nums[1]) {
                int temp = nums[0];
                nums[0] = nums[1];
                nums[1] = temp;
            }
            if (nums[0] < nums[2]) {
                int temp = nums[0];
                nums[0] = nums[2];
                nums[2] = temp;
            }
            System.out.println(nums[0] == nums[1] + nums[2] ? "right" : "wrong");
        }
    }

    public static int pow(String num) {
        int i = Integer.parseInt(num);
        return i * i;
    }

}

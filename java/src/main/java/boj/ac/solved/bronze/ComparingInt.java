package boj.ac.solved.bronze;

import java.util.Scanner;

public class ComparingInt {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int res = Integer.compare(scn.nextInt(), scn.nextInt());
        System.out.println(res == 1 ? '>' : res == 0 ? "==" : '<');
    }

}

package boj.ac.solved.bronze;

import java.util.Scanner;

public class PrintStart1 {

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder star = new StringBuilder();
        for (int i = 0; i < n; i++) {
            System.out.println(star.append("*"));
        }
    }

}

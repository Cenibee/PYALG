package boj.ac.solved.bronze;

import java.io.IOException;
import java.io.InputStream;

public class SumOfNums {

    public static void main(String[] args) throws IOException {
        InputStream is = System.in;
        while(is.read() != '\n');
        int sum = 0;
        int cur;
        while ((cur = is.read()) != '\n') {
            sum += cur - 48;
        }
        System.out.println(sum);
    }

}

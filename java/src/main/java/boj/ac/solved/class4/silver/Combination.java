package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Combination {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        if (m > n / 2)
            m = n - m;

        BigInteger upper = BigInteger.ONE;
        BigInteger bottom = BigInteger.ONE;

        for (int i = 1; i <= m; i++) {
            upper = upper.multiply(BigInteger.valueOf(n--));
            bottom = bottom.multiply(BigInteger.valueOf(i));
        }

        System.out.println(upper.divide(bottom));

        reader.close();
    }

}

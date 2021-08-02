package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class GoodEncrypt {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        BigInteger k = new BigInteger(st.nextToken());
        long l = Integer.parseInt(st.nextToken());

        boolean[] checker = new boolean[(int) l];
        for (int i = 2; i < l; i++) {
            if (checker[i]) continue;
            if (k.mod(BigInteger.valueOf(i)).equals(BigInteger.ZERO)) {
                System.out.println("BAD " + i);
                return;
            } else {
                for (int o = i; o < checker.length; o += i) checker[o] = true;
            }
        }
        System.out.println("GOOD");
        reader.close();
    }
}

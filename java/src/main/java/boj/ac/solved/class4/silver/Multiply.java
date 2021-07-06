package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Multiply {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");

        BigInteger a = BigInteger.valueOf(Long.parseLong(st.nextToken()));
        BigInteger b = BigInteger.valueOf(Long.parseLong(st.nextToken()));
        BigInteger c = BigInteger.valueOf(Long.parseLong(st.nextToken()));

        System.out.println(a.modPow(b, c));

        reader.close();
    }

}

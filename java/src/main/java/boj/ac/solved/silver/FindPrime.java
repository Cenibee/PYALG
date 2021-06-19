package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class FindPrime {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        reader.readLine();

        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;
        while (st.hasMoreElements()) {
            Integer num = Integer.parseInt(st.nextToken());
            map.put(num, map.getOrDefault(num, 0) + 1);
            max = Math.max(max, num);
        }

        int res = 0;
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= max; i++) {
            boolean isPrime = true;

            for (Integer prime : primes) {
                // 소수가 아니면 break
                if (i % prime == 0) {
                    isPrime = false;
                    break;
                } else if (prime > i / 2) {
                    break;
                }
            }
            if (isPrime) {
                primes.add(i);
                res += map.getOrDefault(i, 0);
            }
        }
        System.out.println(res);
    }

}

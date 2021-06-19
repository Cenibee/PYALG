package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class GcdLcm {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        if (a > b) {
            int temp = a; a = b; b = temp;
        }
        if (b % a == 0) {
            System.out.println(String.join("\n", String.valueOf(a), String.valueOf(b)));
            return;
        }

        List<Integer> aPrimes = new ArrayList<>();
        List<Integer> bPrimes = new ArrayList<>();

        for (int i = 2; a != 1 || b != 1 ; i++) {
            while (a % i == 0) {
                aPrimes.add(i);
                a /= i;
            }
            while (b % i == 0) {
                bPrimes.add(i);
                b /= i;
            }
        }

        int gcd = 1;
        int lcm = 1;
        int ap = 0;
        int bp = 0;

        while (ap < aPrimes.size() && bp < bPrimes.size()) {
            int a_ = aPrimes.get(ap);
            int b_ = bPrimes.get(bp);

            if (a_ == b_) {
                ap++; bp++;
                gcd *= a_;
                lcm *= b_;
            } else if (a_ > b_) {
                bp++;
                lcm *= b_;
            } else {
                ap++;
                lcm *= a_;
            }
        }
        while (ap < aPrimes.size()) {
            lcm *= aPrimes.get(ap++);
        }
        while (bp < bPrimes.size()) {
            lcm *= bPrimes.get(bp++);
        }

        System.out.println(String.join("\n", String.valueOf(gcd), String.valueOf(lcm)));
    }

}

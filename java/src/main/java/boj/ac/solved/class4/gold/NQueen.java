package boj.ac.solved.class4.gold;

import java.io.IOException;

public class NQueen {

    public static void main(String[] args) throws IOException {
        int n = System.in.read() - '0';
        if (n == 1) {
            int next = System.in.read();
            if (next != '\n') n = next - '0' + 10;
        }

        if (n == 1) System.out.println(1);
        else if (n == 2 || n == 3) System.out.println(0);
        else {
            boolean[] row = new boolean[n];
            boolean[] lToR = new boolean[2 * n - 1];
            boolean[] rToL = new boolean[2 * n - 1];

            int r = 0;
            int c = 0;
            int[] col = new int[n];
            int result = 0;
            while (true) {
                if (c == n || r == n) {
                    if (c == n) result++;
                    if (--c == -1) break;
                    r = col[c];
                    row[r] = false;
                    rToL[c + r] = false;
                    lToR[n - 1 - c + r] = false;
                    r++;
                } else if (!row[r] && !lToR[n - 1 - c + r] && !rToL[c + r]) {
                    row[r] = true;
                    rToL[c + r] = true;
                    lToR[n - 1 - c + r] = true;
                    col[c] = r;
                    r = 0;
                    c += 1;
                } else {
                    r++;
                }
            }
            System.out.println(result);
        }
    }

}

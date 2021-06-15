package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Olympic {

    public static class TotalMedal implements Comparable<TotalMedal>{
        int gold, silver, bronze;

        public TotalMedal(int gold, int silver, int bronze) {
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        @Override
        public int compareTo(TotalMedal o) {
            if (gold != o.gold) {
                return gold - o.gold;
            } else if (silver != o.silver) {
                return silver - o.silver;
            } else if (bronze != o.bronze) {
                return bronze - o.bronze;
            }
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        Set<TotalMedal> set = new HashSet<>();

        String[] split = reader.readLine().split(" ");
        int total = Integer.parseInt(split[0]);
        int target = Integer.parseInt(split[1]);
        TotalMedal targetMedal = null;

        for (int i = 1; i <= total; i++) {
            String[] s = reader.readLine().split(" ");
            if (Integer.parseInt(s[0]) == target) {
                targetMedal = new TotalMedal(Integer.parseInt(s[1]), Integer.parseInt(s[2]), Integer.parseInt(s[3]));
            } else {
                set.add(new TotalMedal(Integer.parseInt(s[1]), Integer.parseInt(s[2]), Integer.parseInt(s[3])));
            }
        }
        final TotalMedal comp = targetMedal;
        System.out.println(1 + set.stream()
                .filter(totalMedal -> comp.compareTo(totalMedal) < 0)
                .count());

    }

}

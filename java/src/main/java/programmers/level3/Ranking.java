package programmers.level3;

import java.util.HashSet;
import java.util.Set;

public class Ranking {
    private class Ability {
        private final Integer player;
        public Set<Ability> upperEdge;
        public Set<Ability> bottomEdge;
        private Set<Integer> upperSet;
        private Set<Integer> bottomSet;

        public Ability (Integer player) {
            this.player = player;
            upperEdge = new HashSet<>();
            bottomEdge = new HashSet<>();
        }

        public Set<Integer> getUpperSet() {
            if (upperSet == null){
                upperSet = new HashSet<>();
                for (Ability upper : upperEdge) {
                    upperSet.add(upper.player);
                    upperSet.addAll(upper.getUpperSet());
                }
            }
            return upperSet;
        }

        public Set<Integer> getBottomSet() {
            if (bottomSet == null){
                bottomSet = new HashSet<>();
                for (Ability bottom : bottomEdge) {
                    bottomSet.add(bottom.player);
                    bottomSet.addAll(bottom.getBottomSet());
                }
            }
            return bottomSet;
        }
    }

    public int solution(int n, int[][] results) {
        Ability[] abilities = new Ability[n + 1];
        for (int i = 0; i <= n; i++) abilities[i] = new Ability(i);

        for (int[] result : results) {
            abilities[result[0]].bottomEdge.add(abilities[result[1]]);
            abilities[result[1]].upperEdge.add(abilities[result[0]]);
        }

        int answer = 0;
        for (Ability ability : abilities) {
            int count = ability.getUpperSet().size() + ability.getBottomSet().size();
            if (count == n - 1)
                answer++;
        }

        return answer;
    }

}

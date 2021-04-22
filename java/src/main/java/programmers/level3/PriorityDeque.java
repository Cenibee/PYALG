package programmers.level3;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class PriorityDeque {
    class IntPriorityDeque {
        PriorityQueue<Integer> min = new PriorityQueue<>();
        Map<Integer, Integer> removedMin = new HashMap<>();
        PriorityQueue<Integer> max = new PriorityQueue<>(
                Comparator.reverseOrder());
        Map<Integer, Integer> removedMax = new HashMap<>();

        public void add(Integer num) {
            min.add(num);
            max.add(num);
        }

        public Integer pollMin() {
            return pollFrom(min, removedMin, removedMax);
        }

        public Integer pollMax() {
            return pollFrom(max, removedMax, removedMin);
        }

        private Integer pollFrom(PriorityQueue<Integer> target,
                                 Map<Integer, Integer> removedThisSide, Map<Integer, Integer> removedOtherSide) {
            Integer ret = target.poll();
            if (ret == null)
                return 0;
            Integer removedHistory = removedOtherSide.remove(ret);
            while (removedHistory != null) {
                if (removedHistory != 1)
                    removedOtherSide.put(ret, removedHistory - 1);
                ret = target.poll();
                if (ret == null)
                    return 0;
                removedHistory = removedOtherSide.remove(ret);
            }
            removedThisSide.put(ret, removedThisSide.getOrDefault(ret, 0) + 1);
            return ret;
        }
    }

    public int[] solution(String[] operations) {
        IntPriorityDeque queue = new IntPriorityDeque();

        for (String oper : operations) {
            if (oper.startsWith("I"))
                queue.add(Integer.valueOf(oper.substring(2)));
            else if (!oper.contains("-"))
                queue.pollMax();
            else
                queue.pollMin();
        }

        return new int[]{queue.pollMax(), queue.pollMin()};
    }
}

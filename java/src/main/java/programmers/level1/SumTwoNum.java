package programmers.level1;

import java.util.Set;
import java.util.TreeSet;

public class SumTwoNum {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new TreeSet<>();

        for (int i = 0; i < numbers.length; i++)
            for (int o = i + 1; o < numbers.length; o++)
                set.add(numbers[i] + numbers[o]);

        int i = 0;
        int[] answer = new int[set.size()];
        for (Integer val : set) answer[i++] = val;

        return answer;
    }
}

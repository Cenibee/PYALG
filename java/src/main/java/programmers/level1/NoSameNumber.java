package programmers.level1;

import java.util.LinkedList;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12906
 */
public class NoSameNumber {
    public LinkedList<Integer> solution(int []arr) {
        LinkedList<Integer> list = new LinkedList<>();

        for (int val : arr)
            if (list.isEmpty() || list.peekLast() != val)
                list.add(val);

        return list;
    }
}

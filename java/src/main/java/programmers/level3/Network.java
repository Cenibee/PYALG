package programmers.level3;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class Network {
    public int solution(int n, int[][] computers) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) set.add(i);
        int answer = 0;
        LinkedList<Integer> q = new LinkedList<>();
        while (!set.isEmpty()) {
            answer++;
            q.add(set.iterator().next());
            while (!q.isEmpty()) {
                int next = q.pollFirst();
                for (int i = 0; i < n; i++)
                    if (computers[next][i] == 1 && set.remove(i) && i != next)
                        q.add(i);
            }
        }
        return answer;
    }
}

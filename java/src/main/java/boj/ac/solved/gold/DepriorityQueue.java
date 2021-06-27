package boj.ac.solved.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.concurrent.ConcurrentSkipListMap;

public class DepriorityQueue {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        for (int i = 0; i < round; i++) {
            ConcurrentSkipListMap<Integer, Integer> depriorityQueue = new ConcurrentSkipListMap<>();
            int operationCount = Integer.parseInt(reader.readLine());
            for (int o = 0; o < operationCount; o++) {
                StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
                String oper = st.nextToken();
                if ("I".equals(oper)) {
                    int key = Integer.parseInt(st.nextToken());
                    depriorityQueue.put(key, depriorityQueue.getOrDefault(key, 0) + 1);
                } else {
                    if (depriorityQueue.isEmpty()) continue;
                    boolean isLast = "1".equals(st.nextToken());
                    Map.Entry<Integer, Integer> entry = isLast ?
                            depriorityQueue.lastEntry() : depriorityQueue.firstEntry();
                    if (entry.getValue() == 1) {
                        if (isLast)
                            depriorityQueue.pollLastEntry();
                        else
                            depriorityQueue.pollFirstEntry();
                    } else {
                        depriorityQueue.put(entry.getKey(), entry.getValue() - 1);
                    }
                }
            }
            if (depriorityQueue.isEmpty())
                ans.append("EMPTY\n");
            else
                ans.append(depriorityQueue.lastKey()).append(' ')
                    .append(depriorityQueue.firstKey()).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

}

package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class MinHeap {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int operationCount = Integer.parseInt(reader.readLine());

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int i = 0; i < operationCount; i++) {
            int num = Integer.parseInt(reader.readLine());
            if (num == 0)
                ans.append(minHeap.isEmpty() ? 0 : minHeap.poll()).append('\n');
            else
                minHeap.add(num);
        }
        System.out.println(ans);

        reader.close();
    }

}

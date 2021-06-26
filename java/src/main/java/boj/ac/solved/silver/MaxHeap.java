package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MaxHeap {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();
        int num = Integer.parseInt(reader.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>(Comparator.comparingInt(i -> -i));
        for (int i = 0; i < num; i++) {
            int current = Integer.parseInt(reader.readLine());
            if (current == 0) {
                result.append(queue.isEmpty() ? 0 : queue.poll()).append('\n');
            } else {
                queue.add(current);
            }
        }
        System.out.println(result);

        reader.close();
    }

}

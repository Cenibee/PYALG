package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Deque {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        LinkedList<String> deque = new LinkedList<>();
        for (int i = 0; i < round; i++) {
            String line = reader.readLine();
            if (line.startsWith("pop_f")) {
                sb.append(deque.isEmpty() ? "-1" : deque.removeFirst()).append('\n');
            } else if (line.startsWith("pop_b")) {
                sb.append(deque.isEmpty() ? "-1" : deque.removeLast()).append('\n');
            } else if (line.startsWith("push_f")) {
                deque.addFirst(line.substring(11));
            } else if (line.startsWith("push_b")) {
                deque.addLast(line.substring(10));
            } else if (line.startsWith("s")) {
                sb.append(deque.size()).append('\n');
            } else if (line.startsWith("e")) {
                sb.append(deque.isEmpty() ? "1" : "0").append('\n');
            } else if (line.startsWith("f")) {
                sb.append(deque.isEmpty() ? "-1" : deque.getFirst()).append('\n');
            } else if (line.startsWith("b")) {
                sb.append(deque.isEmpty() ? "-1" : deque.getLast()).append('\n');
            }
        }

        System.out.println(sb);
        reader.close();
    }

}

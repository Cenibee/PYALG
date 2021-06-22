package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class QueueCmd {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        LinkedList<String> queue = new LinkedList<>();
        for (int i = 0; i < round; i++) {
            String line = reader.readLine();
            if ("pop".equals(line)) {
                sb.append(queue.isEmpty() ? "-1" : queue.poll()).append('\n');
            } else if (line.startsWith("p")) {
                queue.add(line.substring(line.indexOf(' ') + 1));
            } else if (line.startsWith("s")) {
                sb.append(queue.size()).append('\n');
            } else if (line.startsWith("e")) {
                sb.append(queue.isEmpty() ? "1" : "0").append('\n');
            } else if (line.startsWith("f")) {
                sb.append(queue.isEmpty() ? "-1" : queue.getFirst()).append('\n');
            } else if (line.startsWith("b")) {
                sb.append(queue.isEmpty() ? "-1" : queue.getLast()).append('\n');
            }
        }

        System.out.println(sb);
        reader.close();
    }

}

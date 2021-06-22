package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class StackCmd {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int round = Integer.parseInt(reader.readLine());

        Stack<String> stack = new Stack<>();
        for (int i = 0; i < round; i++) {
            String line = reader.readLine();
            if ("pop".equals(line)) {
                sb.append(stack.isEmpty() ? "-1" : stack.pop()).append('\n');
            } else if (line.startsWith("p")) {
                stack.add(line.substring(line.indexOf(' ') + 1));
            } else if (line.startsWith("s")) {
                sb.append(stack.size()).append('\n');
            } else if (line.startsWith("e")) {
                sb.append(stack.isEmpty() ? "1" : "0").append('\n');
            } else if (line.startsWith("t")) {
                sb.append(stack.isEmpty() ? "-1" : stack.peek()).append('\n');
            }
        }

        System.out.println(sb);
        reader.close();
    }

}

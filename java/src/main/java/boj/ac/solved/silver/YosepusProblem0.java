package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class YosepusProblem0 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder("<");

        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        LinkedList<String> list = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            list.add(String.valueOf(i));
        }

        for (int i = k - 1; list.size() != 1; i = (i + k - 1) % list.size()) {
            sb.append(list.remove(i)).append(", ");
        }
        sb.append(list.get(0)).append(">");
        System.out.println(sb);

        reader.close();
    }

}

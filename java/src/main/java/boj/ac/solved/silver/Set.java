package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Set {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        boolean[] arr = new boolean[21];
        Arrays.fill(arr, false);

        int r = Integer.parseInt(reader.readLine());
        for (int i = 0; i < r; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " " );
            String op = st.nextToken();
            if (op.startsWith("ad")) {
                arr[Integer.parseInt(st.nextToken())] = true;
            } else if (op.startsWith("r")) {
                arr[Integer.parseInt(st.nextToken())] = false;
            } else if (op.startsWith("c")) {
                sb.append(arr[Integer.parseInt(st.nextToken())] ? 1 : 0).append('\n');
            } else if (op.startsWith("t")) {
                int n = Integer.parseInt(st.nextToken());
                arr[n] = !arr[n];
            } else if (op.startsWith("a")) {
                Arrays.fill(arr, true);
            } else if (op.startsWith("e")) {
                Arrays.fill(arr, false);
            }
        }
        System.out.println(sb);
    }

}

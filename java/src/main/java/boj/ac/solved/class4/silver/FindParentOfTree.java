package boj.ac.solved.class4.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class FindParentOfTree {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder ans = new StringBuilder();
        int n = Integer.parseInt(reader.readLine());

        int[] res = new int[n + 1];
        res[1] = -1;
        Set<Integer>[] edges = new Set[n + 1];
        for (int i = 1; i <= n; i++) {
            edges[i] = new HashSet<>();
        }

        for (int i = 1; i < n; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
            edges[b].add(a);
        }

        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(1);

        while (queue.size() != 0) {
            Integer parent = queue.poll();
            for (int child : edges[parent]) {
                if (res[child] == 0) {
                    res[child] = parent;
                    queue.add(child);
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            ans.append(res[i]).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

}

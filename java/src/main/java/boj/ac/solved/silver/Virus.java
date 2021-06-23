package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.*;

public class Virus {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(reader.readLine());
        int edgeNum = Integer.parseInt(reader.readLine());

        Set<Integer>[] edges = new Set[num + 1];
        for (int i = 1; i <= num; i++) {
            edges[i] = new HashSet<>();
        }
        for (int i = 0; i < edgeNum; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
            edges[b].add(a);
        }

        List<Integer> bfs = new ArrayList<>();
        bfs.add(1);

        int res = 0;
        for (int i = 0; i < bfs.size(); i++) {
            Integer next = bfs.get(i);
            Set<Integer> edge = edges[next];
            if (edge == null) continue;
            res++;
            edges[next] = null;
            bfs.addAll(edge);
        }
        System.out.println(res - 1);

        reader.close();
    }

}

package boj.ac.solved.class4.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class ShortestPath {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int vertex = nextInt(st);
        int edge = nextInt(st);
        int start = Integer.parseInt(reader.readLine());

        int[] path = new int[vertex + 1];
        List<List<Integer>>[] edges = new List[vertex + 1];
        for (int i = 0; i <= vertex; i++) {
            edges[i] = new ArrayList<>();
        }
        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int s = nextInt(st);
            edges[s].add(List.of(nextInt(st), nextInt(st)));
        }

        PriorityQueue<List<Integer>> priorityQueue = new PriorityQueue<>(Comparator.comparingInt(l -> l.get(1)));
        priorityQueue.addAll(edges[start]);

        while (!priorityQueue.isEmpty()) {
            List<Integer> poll = priorityQueue.poll();
            int to = poll.get(0);
            int w = poll.get(1);
            if ((path[to] == 0 && to != start) || path[to] > w) {
                path[to] = w;
                for (List<Integer> l : edges[to]) {
                    priorityQueue.add(List.of(l.get(0), l.get(1) + w));
                }
            }
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 1; i < path.length; i++) {
            if (path[i] == 0)
                ans.append(i != start ? "INF\n" : "0\n");
            else
                ans.append(path[i]).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

    private static int nextInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    private static void sol1() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int vertex = nextInt(st);
        int edge = nextInt(st);
        int start = Integer.parseInt(reader.readLine());

        int[] path = new int[vertex + 1];
        List<List<Integer>>[] edges = new List[edge + 1];
        for (int i = 0; i <= vertex; i++) {
            edges[i] = new ArrayList<>();
        }
        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(reader.readLine(), " ");
            int s = nextInt(st);
            edges[s].add(List.of(s, nextInt(st), nextInt(st)));
        }
        Set<List<Integer>> bfs = new HashSet<>(edges[start]);
        while (bfs.size() != 0) {
            Set<List<Integer>> nextBfs = new HashSet<>();
            for (List<Integer> l : bfs) {
                int from = l.get(0);
                int to = l.get(1);
                int w = l.get(2);

                if (path[to] == 0 || path[to] > path[from] + w) {
                    path[to] = path[from] + w;
                    nextBfs.addAll(edges[to]);
                }
            }
            bfs = nextBfs;
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 1; i < path.length; i++) {
            if (path[i] == 0)
                ans.append(i != start ? "INF\n" : "0\n");
            else
                ans.append(path[i]).append('\n');
        }
        System.out.println(ans);

        reader.close();
    }

}

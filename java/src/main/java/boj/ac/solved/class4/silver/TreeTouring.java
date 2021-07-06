package boj.ac.solved.class4.silver;

import java.io.IOException;

public class TreeTouring {
    static Node[] cache;
    static StringBuilder pre = new StringBuilder();
    static StringBuilder mid = new StringBuilder();
    static StringBuilder post = new StringBuilder();

    public static class Node {
        private char value;
        private Node left;
        private Node right;

        public Node(char value) {
            this.value = value;
        }

        public void setLeft(char c) {
            if (c == '.') return;
            this.left = cache[c - 'A'];
        }

        public void setRight(char c) {
            if (c == '.') return;
            this.right = cache[c - 'A'];
        }
    }

    public static void main(String[] args) throws IOException {
        int n = read();
        int temp = read();
        if (temp >= 0) {
            n = 10 * n + temp;
            read();
        }
        cache = new Node[n];
        for (int i = 0; i < n; i++) {
            cache[i] = new Node((char) (i + 'A'));
        }
        for (int i = 0; i < n; i++) {
            Node node = cache[readChar() - 'A'];
            node.setLeft(readChar());
            node.setRight(readChar());
        }

        dfs(cache[0]);
        System.out.println(pre.append('\n').append(mid).append('\n').append(post));
    }

    private static void dfs(Node node) {
        pre.append(node.value);
        if (node.left != null)
            dfs(node.left);
        mid.append(node.value);
        if (node.right != null)
            dfs(node.right);
        post.append(node.value);
    }

    public static char readChar() throws IOException {
        char ret = (char) System.in.read();
        try {
            System.in.read();
        } catch (Exception ignore) {}
        return ret;
    }

    public static int read() throws IOException {
        return System.in.read() - '0';
    }

}

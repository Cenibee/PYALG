package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;

public class Card2 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }

        boolean remove = false;
        while (list.size() != 1) {
            Iterator<Integer> iter = list.iterator();
            while (iter.hasNext()) {
                iter.next();
                if (remove = !remove) {
                    iter.remove();
                }
            }
        }
        System.out.println(list.get(0));
    }

}

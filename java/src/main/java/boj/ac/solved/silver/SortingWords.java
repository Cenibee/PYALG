package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.TreeSet;

public class SortingWords {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(reader.readLine());

        Set<String> words = new TreeSet<>((String str1, String str2) -> {
            if (str1.length() == str2.length())
                return str1.compareTo(str2);
            return str1.length() - str2.length();
        });
        for (int i = 0; i < num; i++) {
            words.add(reader.readLine());
        }
        words.forEach(System.out::println);
    }

}

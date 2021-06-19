package boj.ac.solved.silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class SortByAge {

    public static class PersonAge implements Comparable<PersonAge> {

        protected int age;
        protected String name;

        protected PersonAge(String str) {
            StringTokenizer st = new StringTokenizer(str, " ");
            this.age = Integer.parseInt(st.nextToken());
            this.name = st.nextToken();
        }

        @Override
        public int compareTo(PersonAge other) {
            return Integer.compare(age, other.age);
        }

        @Override
        public String toString() {
            return new StringBuilder().append(age).append(' ').append(name).append('\n').toString();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(reader.readLine());

        List<PersonAge> people = new ArrayList<>();
        for (int i = 0; i < num; i++) {
            people.add(new PersonAge(reader.readLine()));
        }
        people.sort(PersonAge::compareTo);
        StringBuilder sb = new StringBuilder();
        for (PersonAge person : people) {
            sb.append(person.toString());
        }
        System.out.println(sb);
    }
}

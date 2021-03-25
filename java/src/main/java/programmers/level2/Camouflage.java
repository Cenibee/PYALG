package programmers.level2;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

public class Camouflage {
    public int streamSolution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();

        Stream.of(clothes)
                .forEach(strings -> map.put(
                        strings[1],
                        map.getOrDefault(strings[1], 0) + 1));
        if (map.size() == 1)
            return map.values().stream().findFirst().get();
        else
            return map.values()
                    .stream()
                    .reduce(1, ((integer, integer2) -> integer * (integer2 + 1))) - 1;
    }

    public int nonStreamSolution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();

        for (String[] strings : clothes)
            map.put(strings[1], map.getOrDefault(strings[1], 0) + 1);

        int answer = 1;
        for (Integer value: map.values()) {
            if (map.size() == 1)
                return value;
            answer *= value + 1;
        }
        return answer;
    }

}

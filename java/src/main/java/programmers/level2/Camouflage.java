package programmers.level2;

import java.util.HashMap;
import java.util.stream.Stream;

public class Camouflage {
    public int streamSolution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();

        Stream.of(clothes)
                .forEach(strings -> map.put(
                        strings[1],
                        map.getOrDefault(strings[1], -1) + 1));
        if (map.size() == 1)
            return map.values().stream().findFirst().get();
        else
            return map.values()
                    .stream()
                    .reduce(1, ((integer, integer2) -> integer * (integer2 + 1))) - 1;
    }
}

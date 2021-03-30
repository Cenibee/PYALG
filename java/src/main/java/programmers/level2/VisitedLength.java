package programmers.level2;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/49994
 */
public class VisitedLength {
    public int solution(String dirs) {
        int x = 0;
        int y = 0;

        Set<Set<List<Integer>>> set = new HashSet<>();

        for (int i = 0; i < dirs.length(); i++) {
            int _x = x;
            int _y = y;
            char ch = dirs.charAt(i);
            if ('L' == ch) _x -= _x > -5 ? 1 : 0;
            else if('R' == ch) _x += _x < 5 ? 1 : 0;
            else if('D' == ch) _y -= _y > -5 ? 1 : 0;
            else if('U' == ch) _y += _y < 5 ? 1 : 0;
            if (x != _x || y != _y)
                set.add(Set.of(List.of(x, y), List.of(_x, _y)));
            x = _x; y = _y;
        }

        return set.size();
    }
}
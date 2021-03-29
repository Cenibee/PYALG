package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12951#
 */
public class MakeJadenCaseString {
    public String solution(String s) {
        char[] str = s.toLowerCase().toCharArray();
        int spaceIdx, from = 0;
        if ('a' <= str[0] && str[0] <= 'z') str[0] -= 32;
        while((spaceIdx = s.indexOf(' ', from)) > -1) {
            from = spaceIdx + 1;
            if (from >= str.length) break;
            else if ('a' <= str[from] && str[from] <= 'z') str[from] -= 32;
        }
        return new String(str);
    }
}

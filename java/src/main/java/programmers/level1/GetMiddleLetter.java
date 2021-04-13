package programmers.level1;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12903
 */
public class GetMiddleLetter {
    public String solution(String s) {
        return s.substring((s.length() - 1)/2, s.length()/2 + 1);
    }
}

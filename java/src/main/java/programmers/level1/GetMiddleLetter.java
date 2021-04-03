package programmers.level1;

public class GetMiddleLetter {
    public String solution(String s) {
        return s.substring((s.length() - 1)/2, s.length()/2 + 1);
    }
}

package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12985
 * /= 2 , *= 2 관련된 거면 bit 를 생각해보자
 */
public class MatchingSchedule {
    public int solution(int n, int a, int b) {
        a--;b--;
        int round = 1;
        while (true) {
            a /= 2;b /= 2;
            if (a == b) return round;
            round ++;
        }
    }
}

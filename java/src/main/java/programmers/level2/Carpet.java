package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/42842?language=java
 */
public class Carpet {
    public int[] solution(int brown, int yellow) {
        int a = brown - 4;
        int b = (int)Math.sqrt((a * a) - (16 * yellow));
        int[] answer = {(a + b) / 4 + 2, (a - b) / 4 + 2};
        return answer;
    }
}

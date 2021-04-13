package programmers.level1;

import java.util.Stack;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/68935
 */
public class ReverseTernary {
    public int solution(int n) {
        Stack<Integer> stack = new Stack<>();

        while (n > 0) {
            stack.push(n % 3);
            n /= 3;
        }

        int answer = 0;
        int mult = 1;
        while(!stack.isEmpty()) {
            answer += stack.pop() * mult;
            mult *= 3;
        }

        return answer;
    }
}

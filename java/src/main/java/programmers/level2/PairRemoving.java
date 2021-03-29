package programmers.level2;

import java.util.Stack;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12973
 */
public class PairRemoving {
    public int solution(String s)  {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray())
        {
            if (stack.size() == 0 || stack.peek() != ch)
                stack.push(ch);
            else
                stack.pop();
        }
        return stack.isEmpty() ? 1 : 0;
    }
}

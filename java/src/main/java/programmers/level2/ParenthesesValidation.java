package programmers.level2;

import java.util.Stack;

public class ParenthesesValidation {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(')
                stack.push(ch);
            else if(stack.size() == 0 || stack.pop() == ')')
                return false;
        }
        return stack.isEmpty();
    }
}

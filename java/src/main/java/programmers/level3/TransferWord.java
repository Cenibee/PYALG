package programmers.level3;

import java.util.LinkedList;

public class TransferWord {
    public int solution(String begin, String target, String[] words) {
        LinkedList<String> deque = new LinkedList<>();
        deque.add(begin);

        int limit = 0;
        int answer = 0;
        while ((limit = deque.size()) > 0) {
            answer++;
            for (int i = 0; i < limit; i++) {
                String current = deque.pollFirst();
                for (int o = 0; o < words.length; o++) {
                    if (words[o].equals("")) continue;
                    if (isTransferable(current, words[o])) {
                        if (words[o].equals(target)) return answer;
                        deque.add(words[o]);
                        words[o] = "";
                    }
                }
            }
        }
        return 0;
    }

    public boolean isTransferable(String a, String b) {
        boolean checker = false;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) continue;
            else if (checker) return false;
            checker = true;
        }
        return checker;
    }
}

package programmers.level2;

import java.util.ArrayList;
import java.util.List;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12911
 * 왠만한 비트 문제는 비트 연산들로 구현할 수 있을 것 같으니 비트 문제라면 그런 방향으로 고민해보자
 */
public class NextBigNumber {

    public int solution(int n) {
        List<Boolean> bit = new ArrayList<>();
        int oneCount = 0;

        while (n != 0) {
            bit.add(n % 2 == 1);
            n /= 2;
        }
        bit.add(false);
        for (int i = 0; i < bit.size(); i++) {
            if (bit.get(i) && bit.get(i + 1))
                oneCount++;
            else if(bit.get(i) && !bit.get(i + 1)) {
                bit.set(i, false);
                bit.set(i + 1, true);
                for (int o = 0; o < oneCount; o++) bit.set(o, true);
                for (int o = oneCount; o < i - 1; o++) bit.set(o, false);
                break;
            }
        }

        int max = 0;
        int num = 1;
        for (int i = 0; i < bit.size(); i++) {
            if (bit.get(i))
                max += num;
            num *= 2;
        }
        return max;
    }
}

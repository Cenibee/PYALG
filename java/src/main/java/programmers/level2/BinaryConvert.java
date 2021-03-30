package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/70129
 */
public class BinaryConvert {
    public int[] solution(String s) {
        int length = 0;
        for (int i = 0; i < s.length(); i++)
            if (s.charAt(i) == '1')
                length++;
        int countZero = s.length() - length;
        int round = 1;

        while (length != 1) {
            int countOne = 0;
            int n = 0;
            while (length != 0) {
                countOne += length % 2;
                length /= 2;
                n++;
            }
            countZero += n - countOne;
            length = countOne;
            round++;
        }
        return new int[]{round, countZero};
    }
}
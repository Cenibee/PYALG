package programmers.level3;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/43238#
 */
public class Entrance {
    public long solution(int n, int[] times) {

        long left = 0;
        long right = Long.MAX_VALUE;
        long mid = right / 2;

        while (left != mid) {
            long sum = 0;
            for (int time : times) {
                long add = mid / time;
                if (Long.MAX_VALUE - sum <= add) {
                    sum = Long.MAX_VALUE;
                    break;
                }
                sum += add;
            }
            if (sum >= n) right = mid;
            else if(sum < n) left = mid;
            mid = (right - left) / 2 + left;
        }
        return mid + 1;
    }
}

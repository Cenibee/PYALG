package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/12924
 */
public class RepresentNumber {
    public int solution(int n) {
        int left, right, sum, answer;
        left = right = sum = 1;
        answer = 0;
        while (left <= n / 2) {
            if (sum == n) answer++;
            if (sum < n) sum += ++right;
            else if(sum >= n) sum -= left++;
        }
        return answer + 1;
    }
}

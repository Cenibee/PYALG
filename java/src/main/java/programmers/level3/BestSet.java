package programmers.level3;

public class BestSet {
    public int[] solution(int n, int s) {
        int base = s / n;

        if (base == 0) return new int[]{-1};

        int mod = s % n;
        int[] answer = new int[n];
        for (int i = 0; i < answer.length; i++)
            answer[i] = base + (answer.length - i <= mod ? 1 : 0);

        int i = 0;

        return answer;
    }
}

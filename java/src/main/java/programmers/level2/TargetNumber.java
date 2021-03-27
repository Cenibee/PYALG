package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/43165#
 */
public class TargetNumber {
    private int[] numbers;
    private int target;

    private int dfs(int index, int before) {
        if (index < numbers.length - 1)
            return this.dfs(index + 1, before + numbers[index])
                    + this.dfs(index + 1, before - numbers[index]);
        else if (before + numbers[index] == target ||
                before - numbers[index] == target)
            return 1;
        return 0;
    }

    public int solution(int[] numbers, int target) {
        this.target = target;
        this.numbers = numbers;
        return this.dfs(0, 0);
    }
}
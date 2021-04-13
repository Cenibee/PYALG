package programmers.level3;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/43105
 */
public class IntegerTriangle {
    public int solution(int[][] triangle) {
        for (int i = triangle.length - 2; i >= 0; i--)
            for (int o = 0; o <= i; o++)
                triangle[i][o] +=
                        Math.max(triangle[i + 1][o], triangle[i + 1][o + 1]);
        return triangle[0][0];
    }
}

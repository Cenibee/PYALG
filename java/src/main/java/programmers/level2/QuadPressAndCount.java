package programmers.level2;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/68936
 */
public class QuadPressAndCount {
    private int[] dac (int[][] arr, int rFrom, int cFrom, int len) {
        if (len == 1)
            return new int[]{1 - arr[rFrom][cFrom], arr[rFrom][cFrom]};
        len /= 2;
        int[] a = dac(arr, rFrom, cFrom, len);
        int[] b = dac(arr, rFrom + len, cFrom, len);
        int[] c = dac(arr, rFrom, cFrom + len, len);
        int[] d = dac(arr, rFrom + len, cFrom + len, len);
        a[0] += b[0] + c[0] + d[0];
        a[1] += b[1] + c[1] + d[1];
        if (a[0] == 0)
            a[1] = 1;
        else if(a[1] == 0)
            a[0] = 1;
        return a;
    }

    public int[] solution(int[][] arr) {
        return dac(arr, 0, 0, arr.length);
    }
}
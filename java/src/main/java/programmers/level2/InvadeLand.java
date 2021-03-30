package programmers.level2;

public class InvadeLand {
    int solution(int[][] land) {
        int firstIdx = -1;
        int first = 0;
        int second = 0;

        for (int[] arr : land) {
            int _firstIdx = 0;
            int _first = 0;
            int _second = 0;
            for (int o = 0; o < 4; o++) {
                // 이전 행의 최대 인덱스가 아니면 최대값을 더함
                if (o != firstIdx)
                    arr[o] += first;

                    // 이전 행의 최대 인덱스와 겹치면 그 다음값을 더함
                else arr[o] += second;

                if (arr[o] > _first) {
                    if (_first > _second)
                        _second = _first;
                    _first = arr[o];
                    _firstIdx = o;
                }
                else if (arr[o] == _first)
                    _second = arr[o];

                if (_second < arr[o] && arr[o] < _first)
                    _second = arr[o];
            }
            first = _first;
            firstIdx = _firstIdx;
            second = _second;
        }

        int answer = 0;
        for (int i = 0; i < 4; i++)
            answer = Math.max(answer, land[land.length - 1][i]);

        return answer;
    }
}
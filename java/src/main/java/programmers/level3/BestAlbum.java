package programmers.level3;

import java.util.*;

/**
 * https://programmers.co.kr/learn/courses/30/lessons/42579#
 */
public class BestAlbum {
    public List<Integer> solution(String[] genres, int[] plays) {

        Map<String, Integer> genreCount = new HashMap<>();
        Map<String, PriorityQueue<List<Integer>>> map = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            if (!map.containsKey(genres[i]))
                map.put(genres[i], new PriorityQueue<>((List<Integer> l1, List<Integer> l2) -> {
                    if (l1.get(1).equals(l2.get(1)))
                        return l1.get(0) - l2.get(0);
                    return l2.get(1) - l1.get(1);
                }));
            map.get(genres[i]).add(List.of(i, plays[i]));
            genreCount.put(genres[i], genreCount.getOrDefault(genres[i], 0) + plays[i]);
        }

        List<String> genreList = new ArrayList<>(map.keySet());
        genreList.sort(Comparator.comparingInt((String g) -> -genreCount.get(g)));

        List<Integer> res = new ArrayList<>();
        for (String genre : genreList) {
            res.add(map.get(genre).poll().get(0));
            if(!map.get(genre).isEmpty())
                res.add(map.get(genre).poll().get(0));
        }

        return res;
    }
}

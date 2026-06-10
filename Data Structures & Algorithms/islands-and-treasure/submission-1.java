class Solution {
    static final int INF = Integer.MAX_VALUE;

    public void islandsAndTreasure(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(
                m*n,
                new Comparator<List<Integer>>() {
                    @Override
                    public int compare(List<Integer> arg0, List<Integer> arg1) {
                        return arg0.get(0).compareTo(arg1.get(0));
                    }
                });

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    pq.offer(List.of(0, i, j));
                }
            }
        }

        final int[] DIR = new int[]{ 0, 1, 0, -1, 0 };
        while (!pq.isEmpty()) {
            List<Integer> curr = pq.poll();
            for (int i = 0; i < 4; i++) {
                int x = curr.get(1) + DIR[i];
                int y = curr.get(2) + DIR[i + 1];

                if (x < 0 || x >= m || y < 0 || y >= n) {
                    continue;
                }

                if (grid[x][y] == -1 || grid [x][y] != INF) {
                    // if already processed
                    continue;
                }

                grid[x][y] = curr.get(0) + 1;
                pq.offer(List.of(curr.get(0) + 1, x, y));
            }
        }
    }
}

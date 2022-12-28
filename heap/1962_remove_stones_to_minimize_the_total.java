class Solution {
    // O(klog(n)) time | O(n) space - where n is piles.length
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> b - a);
        for (int num: piles) {
            heap.add(num);
        }

        for (int i = 0; i < k; i++) {
            int stones = heap.remove();
            stones -= stones / 2;
            heap.add(stones);
        }
        int totalStones = 0;
        for (int stone: heap) {
            totalStones += stone;
        }
        return totalStones;
    }
}

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = {}

        for word in words:
            freq[word] = freq.get(word,0) + 1
        
        freq_pair = []
        for key, value in freq.items():
            freq_pair.append((-value, key))
        heapq.heapify(freq_pair)

        string = []
        for i in range(k):
            freq, word = heapq.heappop(freq_pair)
            string.append(word)
        return string
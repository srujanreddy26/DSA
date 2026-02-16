class Solution:
    def frequencySort(self, s: str) -> str:
        
        HashMap = {}
        for c in s:
            HashMap[c] = HashMap.get(c,0)+1

        freq_pair = []
        for key, value in HashMap.items():
            freq_pair.append((-value, key))
        heapq.heapify(freq_pair)
        string = []
        while freq_pair:
            freq, key = heapq.heappop(freq_pair)
            string.append(key * (-freq))

        return "".join(string)
        
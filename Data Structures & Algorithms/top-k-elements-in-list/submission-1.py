class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).most_common()
        l = []
        for i in range(k):
            l.append(c[i][0])
        return l
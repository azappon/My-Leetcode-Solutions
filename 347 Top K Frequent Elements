class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create counter set to obtain values and the number of their occurrences
        counter = Counter(nums)
        # find the k most common numbers
        k_common = counter.most_common(k)
        out = []
        # append them and return (could be done altogether)
        for digit, amount in k_common:
            out.append(digit)
        return out

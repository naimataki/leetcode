class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        n = len(candies)

        for i in range(n):
            result.append(candies[i] + extraCandies >= max(candies))

        return result
        
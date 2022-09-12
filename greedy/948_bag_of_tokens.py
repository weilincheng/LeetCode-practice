class Solution:
    # O(nlog(n)) time | O(n) space - where n is the length of the input array
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        while left <= right:
            if tokens[left] > power:
                if score == 0 or left == right: return score
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                power -= tokens[left]
                score += 1
                left += 1
        return score


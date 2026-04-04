class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = defaultdict(int)

        for card in hand:
            counts[card] += 1

        for card in sorted(counts.keys()):
            if counts[card] < 0:
                return False
            while counts[card] > 0:
                for currentCard in range(card, card + groupSize):
                    counts[currentCard] -= 1
                if counts[currentCard] < 0:
                    return False

        return True
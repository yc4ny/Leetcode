class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks_count = []
        suits_count = []
        for rank in ranks:
            ranks_count.append(ranks.count(rank))
        for suit in suits:
            suits_count.append(suits.count(suit))
        if 5 in suits_count:
            return "Flush"
        if 3 in ranks_count or 4 in ranks_count:
            return "Three of a Kind"
        if 2 in ranks_count:
            return "Pair"
        return "High Card"
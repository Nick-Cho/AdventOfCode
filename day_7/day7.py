letter_map = {"T": "B", "J": "1", "Q": "C", "K": "D", "A": "E"}

def classify(hand):
    counts = [hand.count(card) for card in hand if card != "J"]
    if counts == []:
        counts = [0]
    # print (counts)
    j_counts = hand.count("J") 
    
    
    # print(counts)
    if 5 == (max(counts) + j_counts):
        # print(counts, hand, 6)
        return 6
    if 4 == (max(counts) + j_counts):
        # print(counts, hand, 5, j_counts)
        return 5
    if 3 == (max(counts) + j_counts):
        if 2 in counts:
            # print(counts, hand, 4)
            return 4 
        # print(counts, hand, 3)
        return 3
    if counts.count(2) == 4:
        # print(counts, hand, 2)
        return 2
    if 2 == (max(counts) + j_counts):
        # print(counts, hand, 1)
        return 1
    # print(counts, hand, 0)
    return 0


def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])

plays = []

for line in open('test.txt'):
    hand, bid = line.split()
    plays.append((hand, bid))
    
plays.sort(key=lambda play: strength(play[0]))

# print(plays)

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    print(rank, hand, bid)
    total += rank * int(bid)

print(total)
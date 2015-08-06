#https://projecteuler.net/problem=54

class Hand:
    def __init__(self, hand):
        self.cards = [[x, y] for x, y in hand]
        for card in self.cards:
            if card[0] == 'A':
                card[0] = 14
            elif card[0] == 'T':
                card[0] = 10
            elif card[0] == 'J':
                card[0] = 11
            elif card[0] == 'Q':
                card[0] = 12
            elif card[0] == 'K':
                card[0] = 13
            else:
                card[0] = int(card[0])
        self.cards = sorted(self.cards, reverse=True)
        self.suits = self.countMultiples(self.cards, lambda x: x[1])
        values = self.countMultiples(self.cards, lambda x: x[0])
        self.counts = sorted(map(lambda x: (x[1], x[0]), values), reverse=True)
        self.straight = None

    def countMultiples(self, cards, valueFunc):
        counts = {}
        for card in cards:
            check = valueFunc(card)
            if check in counts:
                counts[check] += 1
            else:
                counts[check] = 1
        sortedCounts = sorted([(key, counts[key]) for key in counts], reverse=True)
        return sortedCounts

    def isFlush(self):
        if len(self.suits) == 1:
            return True
        return False

    def isStraight(self):
        if self.straight != None:
            return self.straight
        if len(self.counts) == 5:
            expected = self.cards[0][0]
            for card in self.cards:
                if card[0] != expected:
                    self.straight = False
                    return False
                expected -= 1
            self.straight = True
            return True
        self.straight = False
        return False

    def parseHand(self):
        if self.isFlush() and self.isStraight():
            return (9, self.cards[0][0])
        elif self.counts[0][0] == 4:
            return (8, self.counts[0][1])
        elif self.counts[0][0] == 3 and self.counts[1][0] == 2:
            return (7, self.counts[0][1])
        elif self.isFlush():
            return tuple([6] + [x[0] for x in self.cards])
        elif self.isStraight():
            return (5, self.cards[0][0])
        elif self.counts[0][0] == 3:
            return (4, self.counts[0][1])
        elif self.counts[0][0] == 2 and self.counts[1][0] == 2:
            return tuple([3, self.counts[0][1]] + [x[0] for x in self.cards])
        elif self.counts[0][0] == 2:
            return tuple([2, self.counts[0][1]] + [x[0] for x in self.cards])
        else:
            return tuple([1] + [x[0] for x in self.cards])

    def compareTo(self, other_hand):
        if self.parseHand() > other_hand.parseHand():
            return 1
        else:
            return 2

def getHands():
    f = open('C:/Users/Peng/Desktop/data.txt', 'r')
    data = []
    line = f.readline().rstrip('\n')
    while line != '':
        data.append(line)
        line = f.readline().rstrip('\n')
    f.close()
    return data

#Given a list of hands, returns the number of hands Player 1 (first 5 cards) wins
def numWins(hands):
    wins = 0
    for line in hands:
        cards = line.split(' ')
        hand1 = Hand(cards[:5])
        hand2 = Hand(cards[5:])
        if hand1.compareTo(hand2) == 1:
            wins += 1
    return wins

print numWins(getHands())
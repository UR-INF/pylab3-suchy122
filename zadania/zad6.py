#zadanie6
import random
def deck():
    face = []
    kolor = ["Hearts", "Diamonds", "Clubs", "Spades"]
    royals = ["J", "Q", "K", "A"]
    deck = []

    for i in range(2, 11):
        face.append(str(i))

    for j in range(4):
        face.append(royals[j])

    for k in range(4):
        for l in range(13):
            card = (face[l] + " of " + kolor[k])
            deck.append(card)
    return deck
deck=deck()
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck
def deal(deck,n):
    hands = [deck[i:n*5:n] for i in range(0, n)]
    print(hands)
print(deck)
shuffle_deck(deck)
print(deck)
n=int(input("Ilu graczy?"))
deal(deck,n)
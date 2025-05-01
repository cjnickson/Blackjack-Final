import random, time

# Variables
PlayerHand = []
DealerHand = []
DealerScore = 0
PlayerScore = 0
Deck = []
BlackJack = 21


# Card class that holds each card's value and name.
class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Resets the deck and shuffles it by default.
def resetDeck(shuffle=True):
    global Deck
    Deck = []
    for _ in range(8):
        Deck.append(Card("Ace", [1, 11]))
        Deck.append(Card("2", 2))
        Deck.append(Card("3", 3))
        Deck.append(Card("4", 4))
        Deck.append(Card("5", 5))
        Deck.append(Card("6", 6))
        Deck.append(Card("7", 7))
        Deck.append(Card("8", 8))
        Deck.append(Card("9", 9))
        Deck.append(Card("10", 10))
        Deck.append(Card("Jack", 10))
        Deck.append(Card("Queen", 10))
        Deck.append(Card("King", 10))

    if shuffle:
        random.shuffle(Deck)


# Passes out cards between the player and the dealer.
def createHands():
    global PlayerHand, DealerHand
    PlayerHand = []
    DealerHand = []
    for _ in range(2):
        PlayerHand.append(Deck[0])
        Deck.pop(0)
        DealerHand.append(Deck[0])
        Deck.pop(0)

def getPlayerScore():
    global PlayerScore, PlayerHand
    PlayerScore = 0
    singleValues = []
    multiValues = []
    for card in PlayerHand:
        if isinstance(card.value, int):
            singleValues += [card]
        elif isinstance(card.value, list):
            multiValues += [card]
    for card in singleValues:
        PlayerScore += card.value
    for card in multiValues:
        if PlayerScore + card.value[-1] > BlackJack:
            PlayerScore += card.value[0]
        else:
            PlayerScore += card.value[-1]

def getDealerScore():
    global DealerScore, DealerHand
    DealerScore = 0
    singleValues = []
    multiValues = []
    for card in DealerHand:
        if isinstance(card.value, int):
            singleValues += [card]
        elif isinstance(card.value, list):
            multiValues += [card]
    for card in singleValues:
        DealerScore += card.value
    for card in multiValues:
        if DealerScore + card.value[-1] > BlackJack:
            DealerScore += card.value[0]
        else:
            DealerScore += card.value[-1]

# Function to give cards.
def passOutCard(CardReceiver):
    global PlayerHand, DealerHand, Deck
    if CardReceiver == "Player":
        PlayerHand.append(Deck[0])
        print(f"You drew a {Deck[0].name}.")
        Deck.pop(0)
    elif CardReceiver == "Dealer":
        DealerHand.append(Deck[0])
        print(f"The dealer drew a {Deck[0].name}.")
        Deck.pop(0)
    time.sleep(0.5)


# This function holds the entire gameplay loop, including hitting, standing, the dealers turn, and winning or losing.
def Play():
    global DealerScore, PlayerScore
    string = []
    for i in PlayerHand:
        string += [i.name]
    string = ", ".join(string)
    print(f"\nYour hand is: {string}")

    time.sleep(0.5)
    print(f"\nThe dealers top card is: {DealerHand[-1].name}")
    action = input("\nWould you like to hit or stand? (Type 'Hit' to hit, or 'Stand' to stand): ").lower()
    if action == "hit":
        getPlayerScore()
        if PlayerScore > BlackJack:
            print(f"You cannot hit because your hand's value exceeds {BlackJack}.")
            Play()
        else:
            print("The dealer handed you a card.")
            passOutCard("Player")
            getPlayerScore()
            print(f"Total value of the cards in your hand is: {PlayerScore}")
            Play()
    elif action == "stand":
        print("You chose to stand.")
        print("If you are closer to 21 than the dealer, you win.")
        string = []
        for i in DealerHand:
            string += [i.name]
        string = ", ".join(string)
        print(f"\nThe dealers hand is: {string}")

        time.sleep(0.5)
        getDealerScore()
        if DealerScore < round(BlackJack - 6):
            getDealerScore()
            while True:
                passOutCard("Dealer")
                getDealerScore()
                if DealerScore >= 15:
                    break
        print(f"The dealers total value is: {DealerScore}")
        getPlayerScore()
        print(f"Your total value is: {PlayerScore}")
        if DealerScore > BlackJack:
            DealerScore = 0
        if PlayerScore > BlackJack:
            PlayerScore = 0
        if DealerScore > PlayerScore:
            print("You lose.")

            # You lose the amount of money you bet.

        elif DealerScore < PlayerScore:
            print("You win!")
            if PlayerScore == BlackJack and len(PlayerHand) == 2:
                print("You got a BlackJack! You get increased rewards.")

                # You gain more money than you bet, most likely a 1.5 multiplier rounded.
                # For example (Assuming 'Money' is the amount of money you have and 'BetAmount' is the amount you bet on), Money += round(BetAmount * 1.5)
                # NOTE: This might not work correctly depending on how you implemented the betting system, this is just a guideline/suggestion.

            else:
                pass

                # You gain the amount of money you bet.

        else:
            print("You tied.")

            # You neither gain nor lose the money that you bet.

        if input("Would you like to play again? (Yes/No): ").lower() == "yes":
            return True
        else:
            exit()
    else:
        print("That is not an option.")
        Play()


# Call the functions to play the game
resetDeck()
createHands()
while Play():
    resetDeck()
    createHands()
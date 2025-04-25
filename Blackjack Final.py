import random, time

# Variables
PlayerHand = []
DealerHand = []
DealerScore = 0
PlayerScore = 0
Deck = []
BlackJack = 21


def make_bet():
    global bet
    bet = 0
    print("what amount of chips would you like to bet?")
    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("invalid bet, you only have" + str(chip_pool) + "remaining")


make_bet()
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
        PlayerScore = 0
        for card in PlayerHand:
            if isinstance(card.value, int):
                PlayerScore += card.value
            elif isinstance(card.value, list):
                if PlayerScore + card.value[-1] > BlackJack:
                    PlayerScore += card.value[0]
                else:
                    PlayerScore += card.value[-1]
        if PlayerScore > BlackJack:
            print(f"You cannot hit because your hand's value exceeds {BlackJack}.")
            Play()
        else:
            print("The dealer handed you a card.")
            passOutCard("Player")
            PlayerScore = 0
            for card in PlayerHand:
                if isinstance(card.value, int):
                    PlayerScore += card.value
                elif isinstance(card.value, list):
                    if PlayerScore + card.value[-1] > BlackJack:
                        PlayerScore += card.value[0]
                    else:
                        PlayerScore += card.value[-1]
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
        DealerScore = 0
        for card in DealerHand:
            if isinstance(card.value, int):
                DealerScore += card.value
            elif isinstance(card.value, list):
                if DealerScore + card.value[-1] > BlackJack:
                    DealerScore += card.value[0]
                else:
                    DealerScore += card.value[-1]
        if DealerScore < round(BlackJack / 3.5):
            DealerScore = 0
            for card in DealerHand:
                if isinstance(card.value, int):
                    DealerScore += card.value
                elif isinstance(card.value, list):
                    if DealerScore + card.value[-1] > BlackJack:
                        DealerScore += card.value[0]
                    else:
                        DealerScore += card.value[-1]
            while True:
                passOutCard("Dealer")
                if isinstance(DealerHand[-1].value, int):
                    DealerScore += DealerHand[-1].value
                elif isinstance(DealerHand[-1].value, list):
                    if DealerScore + DealerHand[-1].value[-1] > BlackJack:
                        DealerScore += DealerHand[-1].value[0]
                    else:
                        DealerScore += DealerHand[-1].value[-1]
                if DealerScore >= 15:
                    break
        print(f"The dealers total value is: {DealerScore}")
        PlayerScore = 0
        for card in PlayerHand:
            if isinstance(card.value, int):
                PlayerScore += card.value
            elif isinstance(card.value, list):
                if PlayerScore + card.value[-1] > BlackJack:
                    PlayerScore += card.value[0]
                else:
                    PlayerScore += card.value[-1]
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
    # betting system prototype 1
    chip_pool = 100
    bet = 1



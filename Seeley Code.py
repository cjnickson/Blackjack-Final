#betting system prototype 1
chip_pool =100
bet=1
def make_bet():
    global bet
    bet = 0
    print("what amount of chips would you like to bet?")
    while bet ==0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("invalid bet, you only have" + str(chip_pool) + "remaining")

make_bet()
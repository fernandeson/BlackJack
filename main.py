import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card(pack, number_of_cards):
    for _ in range(0, number_of_cards):
        pack.append(random.choice(cards))
    return pack


def find_winner(user_cards, dealer_cards):
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    while dealer_score < 17:
        dealer_cards = get_card(dealer_cards, 1)
        dealer_score = sum(dealer_cards)
    if dealer_score > 21:
        check_for_ace(dealer_cards)
        dealer_score = sum(dealer_cards)
    if user_score <= 21 and dealer_score <= 21:
        if user_score > dealer_score: print(f"Your cards: {user_cards} --> {user_score}.\nDealer's cards: {dealer_cards} --> {dealer_score}.\n\nYou WIN!!\n")
        elif user_score < dealer_score: print(f"Your cards: {user_cards} --> {user_score}.\nDealer's cards: {dealer_cards} --> {dealer_score}.\n\nYou LOSE!!\n")
        else: print(f"Your cards: {user_cards} --> {user_score}.\nDealer's cards: {dealer_cards} --> {dealer_score}.\n\nIt's a TIE...\n")
    elif user_score > 21:
        print(f"Your cards: {user_cards} --> {user_score}.\nDealer's cards: {dealer_cards} --> {dealer_score}.\n\nYou LOSE!!\n")
    elif dealer_score > 21:
        print(f"Your cards: {user_cards} --> {user_score}.\nDealer's cards: {dealer_cards} --> {dealer_score}.\n\nYou WIN!!\n")

def check_for_ace(pack):
    for i in range(0, len(pack)):
        amount = sum(pack)
        if pack[i] == 11 and amount > 21:
            pack[i] = 1
    return pack

def user_score_check(user_pack, dealer_pack):
    user_amount = sum(user_pack)
    dealer_amount = sum(dealer_pack)
    should_repeat = True
    while should_repeat:
        if user_amount < 21:
            hit_or_stand = input("Would you like another card? y/n: ").lower()
            if hit_or_stand == "y":
                user_pack = get_card(user_pack, 1)
                user_amount = sum(check_for_ace(user_pack))
                print(f"Your cards: {user_pack} --> {user_amount}.\nDealer's first card: {dealer_pack[0]}")
                continue
            if hit_or_stand != "y":
                find_winner(user_cards=user_pack, dealer_cards=dealer_pack)
                break
        elif user_amount == 21:
            if dealer_amount == 21:
                print(f"Your cards: {user_pack} --> {user_amount}.\nDealer's cards: {dealer_pack} --> {dealer_amount}.\n\nIt's a TIE...\n")
                break
            else:
                print(f"Your cards: {user_pack} --> {user_amount}.\nDealer's cards: {dealer_pack} --> {dealer_amount}.\n\n BLACKJACK!! You Win!!\n")
                break
        elif user_amount > 21:
            user_amount = sum(check_for_ace(user_pack))
            if user_amount > 21:
                print("You Lose!!")
                break
            else:
                continue
    wanna_play_again = input("Would you like to play another round? y/n: ")
    if wanna_play_again == "y": play_game()
    else: print("Bye bye!")

def play_game():
    print("\n********************** BLACKJACK **********************\n")

    u_pack = []
    d_pack = []
    get_card(u_pack, 2)
    get_card(d_pack, 2)
    print(f"Your cards: {u_pack}\nDealer's first card: {d_pack[0]}")
    user_score_check(u_pack, d_pack)

play_game()
import random
import os


class Card:
    def __init__(self, card_face, value, symbol):
        self.card_face = card_face
        self.value = value
        self.symbol = symbol


def show_cards(cards, hidden=False):
    lines = [[] for _ in range(9)]
    for card in cards:
        card_lines = [
            f"\t ________________",
            f"\t|                |",
            f"\t|  {card.card_face.center(2)}            |" if card.value == 10 else f"\t|  {card.value}             |",
            f"\t|                |",
            f"\t|                |",
            f"\t|                |",
            f"\t|                |",
            f"\t|       {card.symbol}        |",
            f"\t|                |",
            f"\t|________________|",
        ]
        for i, line in enumerate(card_lines):
            lines[i].append(line)

    if hidden:
        hidden_card_lines = [
            "\t ________________",
            "\t|                |",
            "\t|      * *       |",
            "\t|    *     *     |",
            "\t|   *       *    |",
            "\t|   *       *    |",
            "\t|          *     |",
            "\t|         *      |",
            "\t|        *       |",
            "\t|                |",
            "\t|________________|",
        ]
        for i, line in enumerate(hidden_card_lines):
            lines[i].append(line)

    for line in lines:
        print("".join(line))


def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck


def check_blackjack(score):
    return score == 21


def check_bust(score):
    return score > 21


def change_ace_value(player_cards):
    num_aces = sum(card.card_face == "A" for card in player_cards)
    for card in player_cards:
        if card.card_face == "A" and card.value == 11:
            card.value = 1
            num_aces -= 1
        if num_aces == 0:
            break


def play_blackjack(deck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    os.system("clear")

    for _ in range(2):
        player_card, deck = deal_card(deck)
        player_cards.append(player_card)
        player_score += player_card.value

        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

    if check_blackjack(player_score):
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        quit()

    while True:
        os.system("clear")
        print("DEALER CARDS: ")
        show_cards(dealer_cards[:-1], True)
        print("DEALER SCORE = ", dealer_score - dealer_cards[-1].value)
        print()
        print("PLAYER CARDS: ")
        show_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        choice = input("Enter H to Hit or S to Stand: ").upper()
        if choice == "S":
            break
        elif choice == "H":
            player_card, deck = deal_card(deck)
            player_cards.append(player_card)
            player_score += player_card.value
            change_ace_value(player_cards)

            if check_bust(player_score):
                break
        else:
            print("Invalid choice!! Try Again...")

    os.system("clear")
    print("PLAYER CARDS: ")
    show_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)
    print()
    print("DEALER IS REVEALING THEIR CARDS....")
    print("DEALER CARDS: ")
    show_cards(dealer_cards, False)
    print("DEALER SCORE = ", dealer_score)

    while dealer_score < 17:
        os.system("clear")
        print("DEALER DECIDES TO HIT.....")
        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value
        change_ace_value(dealer_cards)

    if check_bust(dealer_score):
        print("DEALER BUSTED!!! YOU WIN!!!")
        quit()
    elif check_blackjack(dealer_score):
        print("DEALER HAS A BLACKJACK!!! PLAYER LOSES!!!")
        quit()
    elif dealer_score == player_score:
        print("TIE GAME!!!!")
    elif player_score > dealer_score:
        print("PLAYER WINS!!!")
    else:
        print("DEALER WINS!!!")


def init_deck():
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suit_symbols = {"Hearts": "\u2661", "Diamonds": "\u2662", "Spades": "\u2664", "Clubs": "\u2667"}
    cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    deck = [Card(card, value, suit_symbols[suit]) for suit in suits for card, value in cards.items()]
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    deck = init_deck()
    play_blackjack(deck)

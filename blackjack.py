import random
import time

SUITS = ['Spade', 'Diamond', 'Heart', 'Clover']
RANKS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        article = "an" if self.rank in ['Ace', 8] else "a"
        return f"{article} {self.rank} of {self.suit}"

    def value(self):
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank == 'Ace':
            return 11
        else:
            return 10

class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def check(self):
        print(len(self.deck))

def late_print(message):
    print(message)
    time.sleep(2)

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def calculate_total(hand):
    total = sum(card.value() for card in hand)
    num_aces = sum(1 for card in hand if card.rank == 'Ace')
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total


def blackjack():
    late_print('** Welcome to Blackjack!! **')
    deck = Deck()
    dealer_hand = [deck.draw(), deck.draw()]
    player_hand = [deck.draw(), deck.draw()]
    
    late_print(f'Your cards: {player_hand[0]}, {player_hand[1]}')
    late_print(f"Dealer's first card: {dealer_hand[0]}")

    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    
    while player_total < 21 and ask_yes_no("Do you want to draw another card? (yes/no): "):
        player_hand.append(deck.draw())
        late_print(f'Your new card: {player_hand[-1]}')
        player_total = calculate_total(player_hand)

    late_print(f"Dealer's second card: {dealer_hand[1]}")

    while dealer_total < 17 and player_total <= 21:
        dealer_hand.append(deck.draw())
        late_print(f"Dealer draws a card: {dealer_hand[-1]}")
        dealer_total = calculate_total(dealer_hand)

    late_print(f"Dealer's hand: {', '.join(map(str, dealer_hand))}")

    if player_total == 21:
        late_print('BLACK JACK!!! You Win!!!')
    elif player_total > 21:
        late_print('Your hand is over 21! You lose!!')
    elif dealer_total > 21:
        late_print("Dealer's hand is over 21! You win!!")
    elif player_total > dealer_total:
        late_print('You win!')
    elif player_total < dealer_total:
        late_print('Dealer wins!')
    else:
        late_print('It\'s a tie!')

def main():
    while True:
        blackjack()
        if not ask_yes_no("Do you want to play again? (yes/no): "):
            break

main()

import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        random.shuffle(self.deck)
        self.player_hand = []
        self.dealer_hand = []
        self.player_money = 1000
        self.bet = 0

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

    def calculate_score(self, hand):
        score = 0
        ace_count = 0
        for card in hand:
            rank = card['rank']
            if rank in ['Jack', 'Queen', 'King']:
                score += 10
            elif rank == 'Ace':
                ace_count += 1
                score += 11
            else:
                score += int(rank)
        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1
        return score

    def deal_card(self, hand):
        hand.append(self.deck.pop())

    def player_turn(self):
        while True:
            score = self.calculate_score(self.player_hand)
            print(f"Your hand: {self.player_hand}, current score: {score}")
            if score >= 21:
                break
            choice = input("Choose an action: hit/stand/double/split: ").lower()
            if choice == "hit":
                self.deal_card(self.player_hand)
            elif choice == "double":
                if len(self.player_hand) == 2 and self.player_money >= self.bet * 2:
                    self.player_money -= self.bet
                    self.bet *= 2
                    self.deal_card(self.player_hand)
                    break
            elif choice == "split":
                # Implement split functionality here
                pass
            elif choice == "stand":
                break

    def dealer_turn(self):
        while self.calculate_score(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

    def play_round(self):
        if self.player_money <= 0:
            print("You're out of money! Game over.")
            return False

        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0

        # Betting
        while self.bet <= 0 or self.bet > self.player_money:
            try:
                self.bet = int(input("Enter your bet: "))
            except ValueError:
                continue

        self.player_money -= self.bet

        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        # Player's turn
        self.player_turn()

        # Dealer's turn
        if self.calculate_score(self.player_hand) <= 21:
            self.dealer_turn()

        # Determine outcome
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        print(f"Player's final hand: {self.player_hand}, score: {player_score}")
        print(f"Dealer's final hand: {self.dealer_hand}, score: {dealer_score}")

        if player_score > 21:
            result = "Player busts, dealer wins!"
        elif dealer_score > 21 or player_score > dealer_score:
            result = "Player wins!"
            self.player_money += self.bet * 2
        elif player_score < dealer_score:
            result = "Dealer wins!"
        else:
            result = "It's a tie!"
            self.player_money += self.bet

        print(result)
        return True

    def start_game(self):
        while self.play_round():
            pass

# Start the game
game = BlackjackGame()
game.start_game()

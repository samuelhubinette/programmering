import random

def deal_card():
    return random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])

def calculate_hand_value(hand):
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    total_value = sum(values[card] for card in hand)
    num_aces = hand.count("A")

    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

def player_turn(player_hand):
    while True:
        action = input("Vill du ta ett kort (T) eller stanna (S)? ").lower()
        if action == "t":
            player_hand.append(deal_card())
            print(f"Din hand: {player_hand} (Värde: {calculate_hand_value(player_hand)})")
            if calculate_hand_value(player_hand) > 21:
                print("Du har förlorat")
                break
        elif action == "s":
            break
        else:
            print("Ogiltigt val. Vänligen välj T för att ta kort eller S för att stanna.")

def dealer_turn(dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())

def main():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print(f"Din hand: {player_hand} (Värde: {calculate_hand_value(player_hand)})")
    print(f"Dealerns synliga kort: {dealer_hand[0]}")

    player_turn(player_hand)
    dealer_turn(dealer_hand)

    print(f"Dealerns hand: {dealer_hand} (Värde: {calculate_hand_value(dealer_hand)})")

    if calculate_hand_value(player_hand) <= 21 and (calculate_hand_value(dealer_hand) > 21 or calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand)):
        print("Grattis du vann")
    else:
        print("Dealern vinner. Bättre lycka nästa gång!")

if __name__ == "__main__":
    main()

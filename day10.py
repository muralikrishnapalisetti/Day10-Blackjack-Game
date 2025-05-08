import random


# 🃏 Step 1: Deal a random card

def deal_card():
    """Returns a random card from the deck."""
    card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10s represent J, Q, K; 11 = Ace
    return random.choice(card_deck)


# 🧮 Step 2: Calculate score
def calculate_score(hand):
    """
    Takes a list of cards and returns the total score.
    Returns 0 for a Blackjack (2 cards: Ace + 10).
    Converts Ace from 11 to 1 if score goes over 21.
    """
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


# ⚖️ Step 3: Compare user vs dealer score
def compare(user_score, dealer_score):
    """Compares the scores and returns a result string."""
    if user_score == dealer_score:
        return "It's a draw 🙃"
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


# 🕹️ Step 4: Main game logic
def play_blackjack():
    print("Welcome to 🃏 Blackjack 🃏\n")
    print("🔢 Game Rules:")
    print("1. The goal is to get as close to 21 as possible without going over.")
    print("2. Face cards (J, Q, K) count as 10. Ace counts as 11 or 1.")
    print("3. Blackjack (an Ace + 10 on the first two cards) is an automatic win.")
    print("4. You can choose to 'hit' (get another card) or 'stand' (end your turn).")
    print("5. If you or the dealer go over 21, it's a bust and an automatic loss.")
    print("6. Equal scores result in a draw.")
    print("Let's begin!\n")

    user_hand = []
    dealer_hand = []
    game_over = False

    # 🔄 Initial deal
    for _ in range(2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # ⏳ User's turn
    while not game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    # 💻 Dealer's turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    # 🧾 Show final results
    print("\n--- FINAL RESULTS ---")
    print(f"Your final hand: {user_hand}, final score: {calculate_score(user_hand)}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {calculate_score(dealer_hand)}")
    print(compare(calculate_score(user_hand), calculate_score(dealer_hand)))


# 🔁 Replay loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print(r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
          |  \/ K|                            _/ |                
          '------'                           |__/  """)
    play_blackjack()

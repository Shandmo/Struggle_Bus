# Blackjack
# This version doesn't have splitting or insurance.

import random, sys

# Set the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    money = 5000
    while True:
        # Check if we are broke.
        if money <= 0:
            print("You're broke!\n")
            print("Get out goober.")
            sys.exit()

        # show amount left, get bet. Give the p100layer and dealer 2 cards from the deck each.
        print('Cash:', money)
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        # show results of draw, prompt for hit or not
        print('Bet:',bet)
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if player bust
            if get_hand_value(player_hand) > 21:
                break

            # Get player's move, options are H, S, or D.
            move = get_move(player_hand, money - bet)

            if move == 'D':
                # player doubles down, prompt to increase bet
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)
            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                new_card = deck.pop()
                rank, suit = new_card
                print('You drew a {} of {}.'.format(rank,suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S', 'D'):
                # Stand / double down stops player turn
                break

        # Handle dealer actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # dealer hits
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
        
                # check if dealer busts
                if get_hand_value(dealer_hand) > 21:
                    break
                input('Press Enter to continue...\n\n')
        
        # display final results if dealer won or the player.
        
        display_hands(player_hand, dealer_hand, False)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print('Dealer busts! You win {}!.'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${}!'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you.')

            input('Press Enter to continue...\n\n')

# create the functionality
def get_bet(maxBet):
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('See you next time brokie.')
            sys.exit()
        if not bet.isdecimal():
            continue # player didnt enter a number

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # player entered invalid bet.
        
def get_deck():
    # Return a list of (rank, suit) tuples for all 52 cards.
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck 

def display_hands(player_hand, dealer_hand, show_dealer_hand):
    # Show the player's and dealer's cards. Hide the dealer's first card if show_dealer_hand is False.
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards:
        print('PLAYER:', get_hand_value(player_hand))
        display_cards(player_hand)

def get_hand_value(cards):
    # Return the value of the cards. Face cards are worth 10...
    # aces are worth 11 or 1 (this funct picks the most suitable ace value)
    value = 0
    number_of_aces = 0

    # Add the value for non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like(rank, suit)
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('L', 'Q', 'J', 'K'):
            value += 10 # face cards worth 10
        else:
            value += int(rank) # numbered cards are worth their number
    
    # dynamically determine ace value
    value += number_of_aces # Add 1 per ace.
    for i in range(number_of_aces):
        # if another 10 can be added without being >21, do so.
        if value + 10 <= 21:
            value += 10
    return value

def display_cards(cards):
    # display all cards in the cards list.
    rows = ['', '', '', '', ''] # the text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # print the top line of card100
        if card == BACKSIDE:
            # Print a card's back.
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            # print the cards front
            rank, suit = card # the card is a tuple data structure
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
        
        # print each row on the screen:200
        for row in rows:
            print(row)

def get_move(player_hand, money):
    # ask the player for their move, return 'H' for hit, 
    # 'S' for stand, and 'D' for double down.
    while True: # Keep looping until player returns valid move.
        # determine what moves the player can make:
        moves = ['(H)it', '(S)tand']
        # the player can double down on their first move
        # we can tell because they'll have two cards:
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # get the player's move
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move # player has entered valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move # player has entered valid move
        
# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
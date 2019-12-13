import os
import random

# Create a list that will be the deck of cards. 13 cards per suit and 4 suits
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print ("Bye!")
	    exit()

def total(hand):
    total = 0
    for card in hand:
	    if card in ("J", "Q", "K"):
	        total+= 10
	    elif card == "A" and total > 10:
	        total+= 1
	    elif card == "A" and total < 11:
                total+= 11
	    else:
	        total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand, player_hand):
	clear()
	print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
	print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got a Blackjack!\n")
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Sorry, you lose. The dealer got a Blackjack.\n")
		play_again()

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got 21!\n")
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Sorry, you lose. The dealer got 21.\n")
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print ("Sorry. You busted. You lose.\n")
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)
		print ("Dealer busts. You win!\n")
	elif total(player_hand) == total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print ("It's a push! You tied with the dealer!\n")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print ("Congratulations. Your score is higher than the dealer. You win\n")

def game():
#clear the "choice" variable and clear the screen
	choice = 0
	clear()
	print ("WELCOME TO BLACKJACK!\n")
#dealer_hand and player_hand are list variables populated by the "deal" function
    dealer_hand = deal(deck)
	player_hand = deal(deck)
#check to see if either player has blackjack
	blackjack(dealer_hand, player_hand)
#Player hand
	while total(player_hand) < 21:
		print ("The dealer is showing a " + str(dealer_hand[0]))
		print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
#Hit or stand?
        choice = input("Do you want to [H]it or [S]tand: ").lower()
		if choice == 'h':
			hit(player_hand)
			clear()
		elif choice == "s":
			break
#dealers hand
    while total(dealer_hand) < 17:
		hit(dealer_hand)
#score evaluates the hand results
	score(dealer_hand, player_hand)
	play_again()

if __name__ == "__main__":
   game()

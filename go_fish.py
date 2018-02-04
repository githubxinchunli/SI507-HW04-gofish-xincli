import random

deck = [i for i in range(1,14)]*4

def remove_book(hand):
	hand = sorted(hand)
	book = 0
	for i in range(1,14):
		if hand.count(i) == 4:
			count += 1
			while i in hand:
				hand.pop(hand.index(i))
	return book

if __name__ == "__main__":
	print('Game starts!')
	player1_card = []
	player2_card = []
	book1 = 0
	book2 = 0
	for i in range(7):
		index1 = random.randint(0,len(deck)-1)
		player1_card.append(deck[index1])
		deck.pop(index1)
		index2 = random.randint(0,len(deck)-1)
		player2_card.append(deck[index2])
		deck.pop(index2)

	player = "player1"
	while len(deck):
		if player == "player1":
			turn = player1_card
			oponent = player2_card
		else:
			turn = player2_card
			oponent = player1_card
		print(player+": "+str(turn))
		showHand = 1
		while True:
			try:
				askNum = int(input(player+' please choose a card rank you would like to ask the other player if they have (between 1-13): '))
				break
			except ValueError:
				print("Invalid input!")

		if askNum < 1 or askNum >13 or askNum not in turn:
			print("You don't have that rank in your hand.")
		else:
			if askNum not in oponent:
				print("Your oponent doesn't have that card rank.")
				index = random.randint(0,len(deck)-1)
				turn.append(deck[index])
				deck.pop(index)
				if player == "player1":
					book1 += remove_book(turn)
					player = "player2"
				else:
					book2 += remove_book(turn)
					player = "player1"
			else:
				print("Your oponent has that card rank and give them all to you.")
				count = oponent.count(askNum)
				for i in range(count):
					turn.append(askNum)
				while askNum in oponent:
					oponent.pop(oponent.index(askNum))
				if player == "player1":
					book1 += remove_book(turn)
					player = "player2"
				else:
					book2 += remove_book(turn)
					player = "player1"
	if book1 > book2:
		print("Player1 wins.")
	elif book1 < book2:
		print("Player2 wins.")
	else:
		print("Tied.")

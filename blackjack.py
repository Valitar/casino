import numpy as np 

count = 0
cards_dealt = 0

def suits(number_of_decks):
	card_list = 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
	hearts = '_H'
	clubs = '_C'
	diamonds = '_D'
	spades = '_S'
	count = 0
	deck = []
	while count < number_of_decks:
		for i in card_list:
			deck.append(i + hearts)
		for i in card_list:
			deck.append(i + clubs)
		for i in card_list:
			deck.append(i + diamonds)
		for i in card_list:
			deck.append(i + spades)
		count = count + 1
	return deck

def shuffle(deck):
	np.random.shuffle(deck)
	return deck 

def deal(deck):
	card = (deck[0])
	deck.pop(0)
	return card
	
def counter(card, count):
	if ('A') in card or ('K') in card or ('Q') in card or ('J') in card or ('10') in card:
		count = count - 1
	elif ('9') in card or ('8') in card or ('7') in card:
		count = count + 0
	else:
		count = count + 1

	return count


deck = shuffle(suits(1))

while cards_dealt < 10:
	card = deal(deck)
	count = counter(card, count)
	print(card, count)
	cards_dealt = cards_dealt + 1



# print(len(shuffle(suits(1))))


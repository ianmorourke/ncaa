from card import Card
import random

class Deck:
	def __init__(self):
		self.cards = []
		self.build()
		
	def build(self):
		for s in ["Clubs", "Spades", "Hearts", "Diamonds"]:
			for v in range (1, 14):
				self.cards.append(Card(s, v))
				
	def show(self):
		for c in self.cards:
			print(c)
			
	def shuffle(self):
		for i in range(51, 1, -1):
			j = random.randint(0, i)
			# print(i, j)
			self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
			
	def draw_card(self):
		return self.cards.pop()

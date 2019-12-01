from card import Card
from deck import Deck

class Hand:
	def __init__(self):
		self.cards = []
		self.hand_counts = []
		self.straight = 0
		self.flush = 0
		self.quads = 0
		self.trips = 0
		self.pairs = 0
		self.high_card = 0
		self.score = 0
		self.tally()
		self.score_hand()
		
		
	def draw(self, deck):
		self.cards.append(deck.draw_card())
		
	def set_hand(self, _cards):
	  self.cards = _cards
		
	def discard(self, discards, opp):
		dc = []
		for c in discards:
			dc.append(self.cards.pop(int(c) - 1))
		opp.hand.cards = dc
		
	def show(self):
		i = 1
		for c in self.cards:
			print("["+ str(i) + "] " + str(c))
			i += 1
			
	def deal_hand(self, deck):
		for i in range(len(self.cards), 5):
			self.draw(deck)
			
	def eval_hand(self):
	  self.tally()
	  self.set_straight()
	  self.set_flush()
	  self.set_quads()
	  self.set_trips()
	  self.set_pairs()
			
	def tally(self):
	  values = []
	  _hand_counts = []
	  for c in self.cards:
	    values.append(c.value)
	    
	    values.sort()
	    
	    for v in values:
	      if [v, values.count(v)] not in _hand_counts:
	        _hand_counts.append([v, values.count(v)])
	        
	    self.hand_counts = _hand_counts
	    
	def set_straight(self):
	  v = []
	  for c in self.cards:
	    v.append(c.value)
	    
	  v.sort()
	  
	  if v[0] == 1:
	    if (v[1] == 2 & v[2] == 3 & v[3] == 4 & v[4] == 5):
	      self.straight = 5
	    elif (v[1] == 10 & v[2] == 11 & v[3] == 12 & v[4] == 13):
	      self.straight = 14
	  elif (v[1] == v[0] + 1) & (v[2] == v[0] + 2) & (v[3] == v[0] + 3) & (v[4] == v[0] + 4):
	    self.straight = v[4]
	  else:
	    self.straight = 0
	    
	def set_flush(self):
	  if self.cards[0].suit == self.cards[1].suit == self.cards[2].suit == self.cards[3].suit == self.cards[4].suit:
	    v = []
	    for c in self.cards:
	      v.append(c.value)
	    v.sort()
	    if v[0] == 1:
	      self.flush = 14
	    else: 
	      self.flush = v[4]
	    
	    
	def set_quads(self):
	  for c in self.hand_counts:
	    if c[1] == 4:
	      if c[0] == 1:
	        return 14
	      else: 
	        return c[0]
	      
	def set_trips(self):
	  for c in self.hand_counts:
	    if c[1] == 3:
	      if c[0] == 1:
	        return 14
	      else:
	        return c[0]
	      
	def set_pairs(self):
	  p = 0
	  h = 0
	  
	  for c in self.hand_counts:
	    if c[1] == 2:
	      if c[0] == 1:
	        h = 14
	      elif c[0] > h:
	        h = c[0]
	      p += 1
	      
	  if p == 2:
	    h += 13
	    
	  self.pairs = h
	  
	def set_high(self):
	  v = []
	  
	  for c in self.cards:
	    v.append(c.value)
	    
	  v.sort()
	  self.high_card = v[4]
	  
	def show_eval(self):
	  if self.straight > 0 & self.flush > 0:
	    print("Straight Flush")
	  elif self.quads > 0:
	    print("Fours")
	  elif self.trips > 0 & self.pairs > 0:
	    print("Full House")
	  elif self.flush > 0:
	    print("Flush")
	  elif self.straight > 0:
	    print("Straight")
	  elif self.trips:
	    print("Trips")
	  elif self.pairs > 13:
	    print("Two Pairs")
	  elif self.pairs > 0 & self.pairs < 13:
	    print("Pair")
	  else:
	    print("High Card")
	  
	def score_hand(self):
	  if self.straight > 0 & self.flush > 0:
	    if self.straight < 8:
	      return 114
	    elif self.straight < 11:
	      return 115
	    elif self.straight < 14:
	      return 116
	    elif self.straight == 14:
	      return 117
	  elif self.quads > 0:
	    if self.quads < 6:
	      return 108
	    elif self.quads < 10:
	      return 109
	    elif self.quads < 13:
	      return 110
	    elif self.quads < 14:
	      return 111
	    elif self.quads == 14:
	      return 112
	  elif self.trips > 0 & self.pairs > 0:
	    if self.trips < 6:
	      return 104
	    elif self.trips < 10:
	      return 105
	    elif self.trips < 14:
	      return 106
	    elif self.trips == 14:
	      return 107
	  elif self.flush > 0:
	    if self.flush < 9:
	      return 99
	    elif self.flush < 11:
	      return 100
	    elif self.flush < 13:
	      return 101
	    elif self.flush < 14:
	      return 102
	    elif self.flush == 14:
	      return 103
	  elif self.straight > 0:
	    if self.straight < 8:
	      return 95
	    elif self.straight < 11:
	      return 96
	    elif self.straight < 14:
	      return 97
	    elif self.straight == 14:
	      return 98
	  elif self.trips > 0:
	    return self.trips + 80
	  elif self.pairs > 0:
	    if self.pairs < 15:
	      return self.pairs + 59
	    elif self.pairs < 19:
	      return 74
	    elif self.pairs < 21:
	      return 75
	    elif self.pairs < 23:
	      return 76
	    elif self.pairs < 25:
	      return 77
	    elif self.pairs == 25:
	      return 78
	    elif self.pairs == 26:
	      return 79
	    elif self.pairs == 27:
	      return 80
	    elif self.pairs == 28:
	      return 81
	  else:
	    return self.high_card + 46

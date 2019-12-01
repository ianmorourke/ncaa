from deck import Deck
from hand import Hand
from player import Player
from opponent import Opponent

class Exhibition:
  def new_exhibition(player, opp):
    deck = Deck()
    deck.shuffle()
    
    player.hand = Hand()
    player.hand.deal_hand(deck)
    opp.hand 
      
    print("{}'s Turn".format(player.name))
    print("Your hand:")
    player.hand.show()
      
    discards = input("Discards: ").split(" ")
    discards.reverse()
    player.hand.discard(discards, opp)
      
    opp.hand.deal_hand(deck)
    print("Opponent's Hand:")
    opp.hand.show()
    player.hand.deal_hand(deck)
    print("Your hand:")
    player.hand.show()
      
    player.hand.eval_hand()
    player.hand.show_eval()
    p1s = player.hand.score_hand()
    opp.hand.eval_hand()
    opp.hand.show_eval()
    o1s = opp.hand.score_hand()
  
    print("You scored: {}".format(p1s))
    print("Opponent scored: {}".format(o1s))
  
    if p1s > o1s:
      player.wins += 1
      print("You win! Your record is {}-{}".format(player.wins, player.losses))
    elif o1s > p1s:
      player.losses += 1
      print("You lose. Your record is {}-{}".format(player.wins, player.losses))
    else:
      print("Tie game!")

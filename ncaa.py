from deck import Deck
from hand import Hand
from opponent import Opponent
from player import Player
from exhibition import Exhibition

def main():
  keep_playing = 1
  player1 = Player("Ian", "West Virginia University")
  opp1 = Opponent("Pitt", [])
  
  while keep_playing:
    Exhibition.new_exhibition(player1, opp1)
    answer = input("Keep playing? y/n:")
    if answer == 'y':
      Exhibition.new_exhibition(player1, opp1)
    elif answer == 'n':
      print("Game over")
      keep_playing = 0
    else:
      print("Invalid input.")
  
def main_old():
  deck = Deck()
  deck.shuffle()

  player1 = Player("Ian", "West Virginia University")
  opp1 = Opponent("Pitt", [])

  player1.hand = Hand()
  player1.hand.deal_hand(deck)

  player1.hand.show()

  discards = input("Discards: ").split(" ")
  discards.reverse()

  player1.hand.discard(discards, opp1)
  player1.hand.deal_hand(deck)
  print("Your hand:")
  player1.hand.show()

  opp1.hand.deal_hand(deck)

  print("Opponent's hand:")
  opp1.hand.show()
  
  # player1.hand.tally()
  
  # print(player1.hand.hand_counts)
  # player1.hand.set_hand([Card("Clubs", 1), Card("Clubs", 2), Card("Clubs", 3), Card("Clubs", 4), Card("Clubs", 5)])
  player1.hand.eval_hand()
  player1.hand.show_eval()
  p1s = player1.hand.score_hand()
  opp1.hand.eval_hand()
  opp1.hand.show_eval()
  o1s = opp1.hand.score_hand()
  
  print("You scored: {}".format(p1s))
  print("Opponent scored: {}".format(o1s))
  
  if p1s > o1s:
    player1.wins += 1
    print("You win! Your record is {}-{}".format(player1.wins, player1.losses))
  elif o1s > p1s:
    player1.losses += 1
    print("You lose. Your record is {}-{}".format(player1.wins, player1.losses))
  else:
    print("Tie game!")

if __name__ == "__main__":
  main()


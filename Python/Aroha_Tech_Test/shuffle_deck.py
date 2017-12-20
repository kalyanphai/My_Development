# input cards
import sys
sys.setrecursionlimit(2010)
deck = [x for x in xrange(52)]
print deck
count = 1
new_deck = []

def shuffle_deck(card_deck, new_deck, count):
  '''It gives a shuffle count required to get initial card sequence'''
  # input cards for comaprison
  deck = [x for x in xrange(52)]
  
  # Looping over cards to shuffle
  for i, card in enumerate(card_deck):
    if i == 0:
      new_deck.append(card)
      del card_deck[i]
    elif i%2 == 0:
      new_deck.append(card)
      del card_deck[i]
    else:
      card_deck.append(card)
      del card_deck[i]
      
  # Checking for shuffle completion
  if card_deck == []:
    if new_deck == deck:
      count += 1
      print "number of shuffles required: ", count
    else:
      count += 1
      shuffle_deck(new_deck, card_deck, count)
  else:
    shuffle_deck(card_deck, new_deck, count)


shuffle_deck(deck, new_deck, count)

from operator import truediv
import sys, random


#from template
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank







#from template
class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)




class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards


    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    print()

    # determine the type of each hand and print
    hand_type = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card']	# create a list to store type of hand
    hand_points = [10,9,8,7,6,5,4,3,2,1]	# create a list to store points for hand



    #separate lists to hold each players hands
    #separate variables for each players' points
    #separate string for hand type of each player
    p1_hand = []
    p1_points = 0
    p1_hand_type = ''

    p2_hand = []
    p2_points = 0
    p2_hand_type = ''

    p3_hand = []
    p3_points = 0
    p3_hand_type = ''

    p4_hand = []
    p4_points = 0
    p4_hand_type = ''

    p5_hand = []
    p5_points = 0
    p5_hand_type = ''

    #fills in hands
    for s in range(len(self.players_hands)):
      if s ==0:
        p1_hand = self.players_hands[i]
      if s ==1:
        p2_hand = self.players_hands[i]
      if s ==2:
        p3_hand = self.players_hands[i]
      if s ==3:
        p4_hand = self.players_hands[i]
      if s ==4:
        p5_hand = self.players_hands[i]

    #the following 5 blocks of if statements finds and updates each players' hand type and point value

    #player 1
    if self.is_royal(p1_hand)[0]!=0:
      p1_points = self.is_royal(p1_hand)[0]
      p1_hand_type = self.is_royal(p1_hand)[1]

    elif self.is_straight_flush(p1_hand)[0]!=0:
      p1_points = self.is_straight_flush(p1_hand)[0]
      p1_hand_type = self.is_straight_flush(p1_hand)[1]

    elif self.is_four_kind(p1_hand)[0]!=0:
      p1_points = self.is_four_kind(p1_hand)[0]
      p1_hand_type = self.is_four_kind(p1_hand)[1]

    elif self.is_full_house(p1_hand)[0]!=0:
      p1_points = self.is_full_house(p1_hand)[0]
      p1_hand_type = self.is_full_house(p1_hand)[1]

    elif self.is_flush(p1_hand)[0]!=0:
      p1_points = self.is_flush(p1_hand)[0]
      p1_hand_type = self.is_flush(p1_hand)[1]
    
    elif self.is_straight(p1_hand)[0]!=0:
      p1_points = self.is_straight(p1_hand)[0]
      p1_hand_type = self.is_straight(p1_hand)[1]

    elif self.is_three_kind(p1_hand)[0]!=0:
      p1_points = self.is_three_kind(p1_hand)[0]
      p1_hand_type = self.is_three_kind(p1_hand)[1]

    elif self.is_two_pair(p1_hand)[0]!=0:
      p1_points = self.is_two_pair(p1_hand)[0]
      p1_hand_type = self.is_two_pair(p1_hand)[1]

    elif self.is_one_pair(p1_hand)[0]!=0:
      p1_points = self.is_one_pair(p1_hand)[0]
      p1_hand_type = self.is_one_pair(p1_hand)[1]

    elif self.is_high_card(p1_hand)[0]!=0:
      p1_points = self.is_high_card(p1_hand)[0]
      p1_hand_type = self.is_high_card(p1_hand)[1]









    #player two
    if self.is_royal(p2_hand)[0]!=0:
      p2_points = self.is_royal(p2_hand)[0]
      p2_hand_type = self.is_royal(p2_hand)[1]

    elif self.is_straight_flush(p2_hand)[0]!=0:
      p2_points = self.is_straight_flush(p2_hand)[0]
      p2_hand_type = self.is_straight_flush(p2_hand)[1]

    elif self.is_four_kind(p2_hand)[0]!=0:
      p2_points = self.is_four_kind(p2_hand)[0]
      p2_hand_type = self.is_four_kind(p2_hand)[1]

    elif self.is_full_house(p2_hand)[0]!=0:
      p2_points = self.is_full_house(p2_hand)[0]
      p2_hand_type = self.is_full_house(p2_hand)[1]

    elif self.is_flush(p2_hand)[0]!=0:
      p2_points = self.is_flush(p2_hand)[0]
      p2_hand_type = self.is_flush(p2_hand)[1]
    
    elif self.is_straight(p2_hand)[0]!=0:
      p2_points = self.is_straight(p2_hand)[0]
      p2_hand_type = self.is_straight(p2_hand)[1]

    elif self.is_three_kind(p2_hand)[0]!=0:
      p2_points = self.is_three_kind(p2_hand)[0]
      p2_hand_type = self.is_three_kind(p2_hand)[1]

    elif self.is_two_pair(p2_hand)[0]!=0:
      p2_points = self.is_two_pair(p2_hand)[0]
      p2_hand_type = self.is_two_pair(p2_hand)[1]

    elif self.is_one_pair(p2_hand)[0]!=0:
      p2_points = self.is_one_pair(p2_hand)[0]
      p2_hand_type = self.is_one_pair(p2_hand)[1]

    elif self.is_high_card(p2_hand)[0]!=0:
      p2_points = self.is_high_card(p2_hand)[0]
      p2_hand_type = self.is_high_card(p2_hand)[1]







    #player three
    if self.is_royal(p3_hand)[0]!=0:
      p3_points = self.is_royal(p3_hand)[0]
      p3_hand_type = self.is_royal(p3_hand)[1]

    elif self.is_straight_flush(p3_hand)[0]!=0:
      p3_points = self.is_straight_flush(p3_hand)[0]
      p3_hand_type = self.is_straight_flush(p3_hand)[1]

    elif self.is_four_kind(p3_hand)[0]!=0:
      p3_points = self.is_four_kind(p3_hand)[0]
      p3_hand_type = self.is_four_kind(p3_hand)[1]

    elif self.is_full_house(p3_hand)[0]!=0:
      p3_points = self.is_full_house(p3_hand)[0]
      p3_hand_type = self.is_full_house(p3_hand)[1]

    elif self.is_flush(p3_hand)[0]!=0:
      p3_points = self.is_flush(p3_hand)[0]
      p3_hand_type = self.is_flush(p3_hand)[1]
    
    elif self.is_straight(p3_hand)[0]!=0:
      p3_points = self.is_straight(p3_hand)[0]
      p3_hand_type = self.is_straight(p3_hand)[1]

    elif self.is_three_kind(p3_hand)[0]!=0:
      p3_points = self.is_three_kind(p3_hand)[0]
      p3_hand_type = self.is_three_kind(p3_hand)[1]

    elif self.is_two_pair(p3_hand)[0]!=0:
      p3_points = self.is_two_pair(p3_hand)[0]
      p3_hand_type = self.is_two_pair(p3_hand)[1]

    elif self.is_one_pair(p3_hand)[0]!=0:
      p3_points = self.is_one_pair(p3_hand)[0]
      p3_hand_type = self.is_one_pair(p3_hand)[1]

    elif self.is_high_card(p3_hand)[0]!=0:
      p3_points = self.is_high_card(p3_hand)[0]
      p3_hand_type = self.is_high_card(p3_hand)[1]


    #player four
    if self.is_royal(p4_hand)[0]!=0:
      p4_points = self.is_royal(p4_hand)[0]
      p4_hand_type = self.is_royal(p4_hand)[1]

    elif self.is_straight_flush(p4_hand)[0]!=0:
      p4_points = self.is_straight_flush(p4_hand)[0]
      p4_hand_type = self.is_straight_flush(p4_hand)[1]

    elif self.is_four_kind(p4_hand)[0]!=0:
      p4_points = self.is_four_kind(p4_hand)[0]
      p4_hand_type = self.is_four_kind(p4_hand)[1]

    elif self.is_full_house(p4_hand)[0]!=0:
      p4_points = self.is_full_house(p4_hand)[0]
      p4_hand_type = self.is_full_house(p4_hand)[1]

    elif self.is_flush(p4_hand)[0]!=0:
      p4_points = self.is_flush(p4_hand)[0]
      p4_hand_type = self.is_flush(p4_hand)[1]
    
    elif self.is_straight(p4_hand)[0]!=0:
      p4_points = self.is_straight(p4_hand)[0]
      p4_hand_type = self.is_straight(p4_hand)[1]

    elif self.is_three_kind(p4_hand)[0]!=0:
      p4_points = self.is_three_kind(p4_hand)[0]
      p4_hand_type = self.is_three_kind(p4_hand)[1]

    elif self.is_two_pair(p4_hand)[0]!=0:
      p4_points = self.is_two_pair(p4_hand)[0]
      p4_hand_type = self.is_two_pair(p4_hand)[1]

    elif self.is_one_pair(p4_hand)[0]!=0:
      p4_points = self.is_one_pair(p4_hand)[0]
      p4_hand_type = self.is_one_pair(p4_hand)[1]

    elif self.is_high_card(p4_hand)[0]!=0:
      p4_points = self.is_high_card(p4_hand)[0]
      p4_hand_type = self.is_high_card(p4_hand)[1]
    

    #player 5 
    if self.is_royal(p5_hand)[0]!=0:
      p5_points = self.is_royal(p5_hand)[0]
      p5_hand_type = self.is_royal(p5_hand)[1]

    elif self.is_straight_flush(p5_hand)[0]!=0:
      p5_points = self.is_straight_flush(p5_hand)[0]
      p5_hand_type = self.is_straight_flush(p5_hand)[1]

    elif self.is_four_kind(p5_hand)[0]!=0:
      p5_points = self.is_four_kind(p5_hand)[0]
      p5_hand_type = self.is_four_kind(p5_hand)[1]

    elif self.is_full_house(p5_hand)[0]!=0:
      p5_points = self.is_full_house(p5_hand)[0]
      p5_hand_type = self.is_full_house(p5_hand)[1]

    elif self.is_flush(p5_hand)[0]!=0:
      p5_points = self.is_flush(p5_hand)[0]
      p5_hand_type = self.is_flush(p5_hand)[1]
    
    elif self.is_straight(p5_hand)[0]!=0:
      p5_points = self.is_straight(p5_hand)[0]
      p5_hand_type = self.is_straight(p5_hand)[1]

    elif self.is_three_kind(p5_hand)[0]!=0:
      p5_points = self.is_three_kind(p5_hand)[0]
      p5_hand_type = self.is_three_kind(p5_hand)[1]

    elif self.is_two_pair(p5_hand)[0]!=0:
      p5_points = self.is_two_pair(p5_hand)[0]
      p5_hand_type = self.is_two_pair(p5_hand)[1]

    elif self.is_one_pair(p5_hand)[0]!=0:
      p5_points = self.is_one_pair(p5_hand)[0]
      p5_hand_type = self.is_one_pair(p5_hand)[1]

    elif self.is_high_card(p5_hand)[0]!=0:
      p5_points = self.is_high_card(p5_hand)[0]
      p5_hand_type = self.is_high_card(p5_hand)[1]

    #fills in all players' data into corresponding lists
    hand_types = [p1_hand_type, p2_hand_type, p3_hand_type, p4_hand_type, p5_hand_type]
    player_points = [p1_points, p2_points, p3_points, p4_points, p5_points]
    player_name = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']

    #prints out player hand type info
    for i in range(len(self.players_hands)):
      print(player_name[i]+': '+hand_types[i])


    #determines winning hand and which player has won
    winner_pts_index = player_points.index(max(player_points))
    winning_hand = hand_types[winner_pts_index]

    #empty array storing the index of the players that have the winning hand
    ties = []

    for j in range(len(self.players_hands)):
      if hand_types[j] == winning_hand:
        ties.append(j)


    #condtional statement checking if a tie exists, if so compares players' point value and prints in descending order
    #else, prints out winner
    if len(ties)>1:
      tie_breaker_pts = []
      for x in ties:
        tie_breaker_pts.append(player_points[x])

      tie_breaker_pts = sorted(tie_breaker_pts, reverse= True)

      for p in ties:
        print('Player '+ str(player_points.index(tie_breaker_pts[p]+1)) + ' ties.')
      else:
        print('Player '+ str(player_points.index(max((player_points)))+1) + ' wins.')    

    # determine winner and print

  # from template
  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'



  #using same logic from royal, but taking out face card and 10 condition
  def is_straight_flush (self, hand):

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)-1):
      rank_order = rank_order and (hand[i].rank == hand[i+1].rank+1)

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'



  #checks if there exists 4 cards in the hand that have the same rank. If so, num_sim_rank will equal 4.
  def is_four_kind (self, hand):

    base_rank = hand[0].rank
    num_sim_rank = 1
    final_rank = hand[0].rank

    for i in range (1,len(hand)):
      
      if num_sim_rank==4:
        final_rank = base_rank
        break
      
      
      if (hand[i].rank == base_rank):
        num_sim_rank+=1
        continue
      else:
        base_rank = hand[i].rank
        num_sim_rank = 1

    #finds side card rank
    four_card_rank = 0
    side_card_rank = []
    for j in range(len(hand)):
      if hand[j].rank!= final_rank:
        side_card_rank.append(hand[j])
      else:
        four_card_rank = hand[j].rank


    if (num_sim_rank!=4):
      return 0, ''

    
    points = 8 * 15 ** 5 + (four_card_rank) * 15 ** 4 + (four_card_rank) * 15 ** 3
    points = points + (four_card_rank) * 15 ** 2 + (four_card_rank) * 15 ** 1
    points = points + (side_card_rank[0].rank)

    return points, 'Four of a Kind'

    

  #checks if 3 cards share a rank and the other two share a rank. If so, there will be a 3 and 3 somewhere in the checks list.
  def is_full_house (self, hand):
    checks = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for card in hand:
      checks[(card.rank-2)]+=1

    if (sum(checks)!=5) or ((not 3 in checks)) or (not 2 in checks):
      return 0, ''

  
    triple_rank = 0
    double_rank = 0

    #finds the rank of the triple and double cards
    triple_rank = checks.index(3)+2
    double_rank = checks.index(2)+2

    points = 7 * 15 ** 5 + (triple_rank) * 15 ** 4 + (triple_rank) * 15 ** 3
    points = points + (triple_rank) * 15 ** 2 + (double_rank) * 15 ** 1
    points = points + (double_rank)

    return points,'Full House'

  #from royal function, without rank.
  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Flush'


  #from royal function, without suit.
  def is_straight (self, hand):

    rank_order = True
    for i in range (len(hand)-1):
      rank_order = rank_order and (hand[i].rank == hand[i+1].rank+1)

    if (not rank_order):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'

    
  #same logic used as in four of a kind, but sets exit condition to num_sim_rank ==3 as opposed to 4.
  def is_three_kind (self, hand):

    base_rank = hand[0].rank
    num_sim_rank = 1
    final_rank = hand[0].rank

    for i in range (1,len(hand)):
      
      if num_sim_rank==3:
        final_rank = base_rank
        break
      
      
      if (hand[i].rank == base_rank):
        num_sim_rank+=1
        continue
      else:
        base_rank = hand[i].rank
        num_sim_rank = 1

    three_card_rank = 0
    side_card_rank = []
    for j in range(len(hand)):
      if hand[j].rank!= final_rank:
        side_card_rank.append(hand[j])
      else:
        three_card_rank = hand[j].rank


    if (num_sim_rank!=3):
      return 0, ''

    side_card_rank = sorted(side_card_rank,reverse=True)

    points = 4 * 15 ** 5 + (three_card_rank) * 15 ** 4 + (three_card_rank) * 15 ** 3
    points = points + (three_card_rank) * 15 ** 2 + (side_card_rank[0].rank) * 15 ** 1
    points = points + (side_card_rank[1].rank)

    return points, 'Three of a Kind'


  # same logic used in full house function. Additional methods are there to find the rank of the remaining cards in the hand.
  def is_two_pair (self, hand):

    checks = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for card in hand:
      checks[(card.rank-2)]+=1

    counter=0
    for checker in checks:
      if checker==2:
        counter+=1

    if (sum(checks)!=5) or (counter!=2):
      return 0, ''

    
    higher_rank = 0
    lower_rank = 0

    temp_rank1 = 0
    temp_rank2 = 0
    #sets temp rank 1, then takes it out of list
    for i in range(len(checks)):
      if checks[i]==2:
        temp_rank1 = checks[i]
        checks[i] = 0
        break

    #sets temp rank two
    for i in range(len(checks)):
      if checks[i]==2:
        temp_rank2 = checks[i]

    #finds higher and lower rank
    if temp_rank1>temp_rank2:
      higher_rank = temp_rank1
      lower_rank = temp_rank2
    else:
      higher_rank = temp_rank2
      lower_rank = temp_rank1

    # finds the remaining card's rank
    side_card_rank = 0
    for card in hand:
      if (card.rank!=higher_rank) or (card.rank!=lower_rank):
        side_card_rank = card.rank

    points = 3 * 15 ** 5 + (higher_rank) * 15 ** 4 + (higher_rank) * 15 ** 3
    points = points + (lower_rank) * 15 ** 2 + (lower_rank) * 15 ** 1
    points = points + (side_card_rank)

    return points,'Two Pair'

    
  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  #similar logic used in two_pair
  def is_one_pair (self, hand):
    one_pair = False

    pair_rank = []
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        pair_rank.append(hand[i].rank)
        pair_rank.append(hand[i+1].rank)
        hand.pop(i+1)
        hand.pop(i)
        break

    hand = sorted(hand, reverse = True)
    
    if (not one_pair):
      return 0, ''

    points = 2 * 15 ** 5 + (pair_rank[0]) * 15 ** 4 + (pair_rank[1]) * 15 ** 3
    points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
    points = points + (hand[2].rank)

    return points, 'One Pair'


  # if no other hand is found to be true, the card is a high card.
  def is_high_card (self,hand):
    
    high_card = False
    if (self.is_royal(hand)[0]==0) and (self.is_straight_flush(hand)[0]==0) and (self.is_four_kind(hand)[0]==0) and (self.is_full_house(hand)[0]==0) and (self.is_flush(hand)[0]==0) and (self.is_straight(hand)[0]==0) and (self.is_three_kind(hand)[0]==0) and (self.is_two_pair(hand)[0]==0) and (self.is_one_pair(hand)[0]==0):
      high_card = True



    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)


    if high_card:
      return points, 'High Card'
    else:
      return

def main():
  #read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker(num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()

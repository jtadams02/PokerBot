##poker player strategy and i/o

import random, pokerhands
from collections import Counter
from operator import attrgetter

class Card:

    RANKS=['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']

    SUITS=['h', 'c', 's', 'd']

    def __init__(self,rank, suit, faceup=True):

        self.rank=rank
        self.suit=suit
        self.values=[]
        self.__value=(Card.RANKS.index(self.rank)+1)
        
        self.faceup=faceup

    def __str__(self):

        if self.faceup:
            
            return str(self.rank)+str(self.suit)
        else:
            return 'XX'

    @property

    def value(self):

        v=self.__value

        return v

def evaluate(player):
	
	value=player.get_value()
	
def calc_bet(player):

                   
        max_bet=player.stack-player.to_play
        min_bet=player.to_play
        if max_bet<min_bet:
        	min_bet=max_bet
        print ('max bet '+str(max_bet))
        print ('min be  '+str(min_bet))
        
        

        if max_bet<0:
                max_bet=player.stack
				
        bet_amount=random.randrange(min_bet,max_bet+1,5)
        
        
        return bet_amount
	

class Strategy():
        
        def __init__(self, player):
                
                self.tight=0
                self.aggression=0
                self.cool=0
                self.player=player
                self.name=str(self.__class__.__name__)

        
              
        @property
        
        def play_style(self):
                
                pass

        def decide_play(self, player, pot):
                
                pass

class SklanskySys2(Strategy):

        #sklansky all-in tournament strategy

        def decide_play(self, player, pot):

                total_blinds=(pot.blinds[0]+pot.blinds[1])
                score=(player.stack/total_blinds)
                score*=pot.yet_to_play
                score*=(pot.limpers+1)
                score=int(score)
                
                hand_value, rep, tie_break, raw_data=player.get_value()
                raw_values, flush_score, straight, gappers=raw_data
                raw_values.sort()
                
                key=((range(0,19)), (range(20,39)), (range(40,59)), (range(60,79)), (range(80,99)), (range(100,149)), (range(150,199)), (range(200, 399)), (range(400, 1000)))

                for k in key:
                	if score in k:
                		pointer=key.index(k)

                GAI=False

                print ('score='+str(score))
                print ('pot raised='+str(pot.raised))
                
                if pot.raised:

                        if raw_values in ((13,13), (12,12)):
                                GAI=True

                        elif raw_values in (13,12) and flush_value==2:
                                GAI=True

                        else:
                                GAI=False
                
                elif score>400 and raw_values in (13,13):
                        GAI=True
                elif score in range (200,399) and raw_values in ((13,13),(12,12)):
                        GAI=True
                elif score in range (150,199) and raw_values in ((13,13),(12,12), (11,11), (13,12)):
                        GAI=True
                elif score in range (100,149) and raw_values in ((13,13),(12,12),(11,11),(10,10),(9,9),(13,12),(13,11),(12,11)):
                        GAI=True
                elif score in range (80,99):
                        if 'pair' in rep:
                                GAI=True
                        elif raw_values in ((13,12),(13,11),(12,11)):
                                GAI=True
                        elif flush_score==2 and 13 in raw_values:
                                GAI=True
                        elif flush_score==2 and straight>=5:
                                GAI=True
                elif score in range (60,79):
                        if 'pair' in rep:
                                GAI=True
                        elif 13 in raw_values:
                                GAI=True
                        elif flush_score==2 and 12 in raw_values:
                                GAI=True
                        elif flush_score==2 and gappers<=1:
                                GAI=True
                elif score in range (40,59):
                        if 'pair' in rep:
                                GAI=True
                        elif 13 or 12 in raw_values:
                                GAI=True
                        elif flush_score==2 and 12 in raw_values:
                                GAI=True
                        elif flush_score==2 and gappers<=1:
                                GAI=True
                elif score in range (20,39):
                        if 'pair' in rep:
                                GAI=True
                        elif 13 or 12 in raw_values:
                                GAI=True
                        elif flush_score==2:
                                GAI=True
                elif score in range(0,19):
                        GAI=True

                else:
                        GAI=False


                if GAI:
                        if player.stack<=player.to_play:
                                player.check_call(pot)
                        else:
                                player.bet(pot, player.stack)
                else:
                        player.fold(pot)
                        
                        
                

##Key Number = 400 or more: Move in with AA and fold everything else.
##Key Number = 200 to 400: Move in with AA and KK only.
##Key Number = 150 to 200: Move in with AA, KK, QQ and AK
##Key Number = 100 to 150: Move in with AA, KK, QQ, JJ, TT, AK, AQ and KQ
##Key Number = 80 to 100: Move in with any pair, AK, AQ, KQ, any suited Ace and
##any suited connector down to 5-4 suited.
##Key Number = 60 to 80: Move in with any pair, any ace, KQ, any suited king
##and all one-gap and no-gap suited connectors.
##Key Number = 40 to 60: Move in with everything above + any king.
##Key Number = 20 to 40: Move in with everything above + any 2 suited cards
##Key Number = <20: Move in with any 2-cards.


class Random(Strategy):

    
        def decide_play(self, player, pot):

                
             
                choice=random.randint(0,3)
               
                
                if choice==0:
                	player.fold(pot)
                
                elif choice==1:
                	if player.stack<=player.to_play:
                		player.check_call(pot)
                	else:
                		player.bet(pot, calc_bet(player))
                elif choice==2:
                	if player.stack<=player.to_play:
                		player.check_call(pot)
                	else:
                		player.bet(pot, player.stack)
                	
                
                
                
		
class Human(Strategy):
    
    options=[['x', 'f', 'b'], ['c', 'r', 'f'], ['c', 'f']]
    choices={0:'check, fold or bet', 1:'call, raise, fold', 2:'call all-in or fold'}
    
    def decide_play(self, player, pot):
        
        player.get_value()
        
        options=Human.options
        choices=Human.choices
        action=''
        op=0


        if player.to_play==0:
                op=0 # Can check
        elif player.to_play<player.stack:
                op=1 # Call
        else: op=2

        

        while action not in options[op]:

                try:
                        action=input(str(choices[op]))
                except NameError:
                 print ('enter a valid choice')

    
        if action=='x':
                player.check_call(pot)
        elif action=='f':
                player.fold(pot)
        elif action=='c':
                player.check_call(pot)
        elif action=='b' or action=='r':
                stake=0
                max_bet=player.stack
                print ('max '+str(max_bet))
                while stake not in range (10,(max_bet+1), 5):
                        try:
                                stake=int(input('stake..'))
                        except:
                                print ('input a stake')
                print ('stake '+str(stake))                                
                player.bet(pot, stake)

        
                                
class JTAdams(Strategy):
        options=[['x', 'f', 'b'], ['c', 'r', 'f'], ['c', 'f']]
        choices={0:'check, fold or bet', 1:'call, raise, fold', 2:'call all-in or fold'}
        names = {1:'deuce', 2:'three', 3:'four', 4:'five', 5:'six', 6:'seven', 7:'eight', 8:'nine', 9:'ten', 10:'jack', 11:'queen', 12:'king', 13:'ace'}
        previous_pots = [] # This will hold information ertaining to the table. Previous pot, etc.

        def decide_play(self, player, pot):
                # So, what we are going to do is evaluate the score of my hand
                # Then generate, lets say 1000 random other hands, and eval their score
                # Then, if my hand is better than a certain percentage
                score, hand_str, tie_break, raw_data = player.get_value()
                # Now we need to generate a ton of random hands
                table_cards = []
                for card in player.total_cards:
                        if card not in player.cards:
                                table_cards.append(card)
                
                wins = 0
                losses = 0
                for i in range(10000):
                        hand = self.gen_hand(player.cards,table_cards)
                        # print(hand)
                        hand_score = self.score(hand)
                        if hand_score > score:
                                losses += 1
                        else:
                                wins += 1
                
                total_games = wins + losses
                print(f'Wins: {wins}')
                print(f'Losses: {losses}')

                win_percentage = (wins/total_games)
                if win_percentage > 0.5:
                        # TODO: Bet something
                        player.bet(pot,round(player.stack*0.2))
                elif win_percentage > 0.4:
                        player.check_call(pot)
                else:
                        player.fold(pot)

        # Return numeric amount to bet
        # TODO: Figure out a way to calculate "potential score"
        def determine_move(self, score, pot, to_call, chips,stage):
                return 0
                
        # This will generate a score for the a random hand!
        # TODO: Ensure that duplicate cards CANNOT be used!
        def gen_hand(self,my_hand,table_hand):
                card1 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
                card2 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
                full_hand = [card1,card2]
                return full_hand
                
        
        # This will generate a score for the given hand
        def score(self,hand):
                score = 0
                values = []
                suits = []
                raw_values = []
                for card in hand:
                        values.append(card.value)  # Append the value of the card to values list
                        suits.append(card.suit)    # Append the suit of the card to suits list
                
                raw_values = values[:]

                # Counter!
                value_count = Counter(values)
                suit_count = Counter(suits)

                # Put values in order of rank
                values.sort(reverse=True)

                pair = []
                trip = []
                quad = []
                multiples = [0,0,pair,trip,quad] # Stores multiple pairs, trips 
                remove_list = [] # List of multiples to be removed
                rep = '' # Represents hand rank
                hand_value = 0 # Represent the VALUE of the HAND TODO: Make this important
                tie_break = 0 # Tiebreaking? Idk what that does
                winning_cards = [] # Store possible cards
                limit = len(values)
                if limit > 5:
                        limit = 5 # I dont know why this is here
                
                # So first thing first, I think we should determine
                # The possiblity of a straight happening
                straight = self.is_straight(values)
                straight_prob = 0
                if straight == -1:
                        straight = 0
                        straight_prob = 1
                flush = 0
                for key, value in suit_count.items():
                        flush_score = 0
                        if value == 5:
                                flush = 1  # Set flush flag to True
                                high_card = 0  # Set high_card flag to False
                        else:
                                flush_score = value  # Update flush_score 

                for key, value in value_count.items():
                        if value > 1:
                                # this is atleast a pair
                                high_card = False
                                multiples[value].append(key)
                                for element in values:
                                        if element == key:
                                                remove_list.append(element)
                                                winning_cards.append(element)
                                # Remove elements from the values list
                                for item in remove_list:
                                        values.remove(item)
                                winning_cards.sort(reverse=True)
                                tie_break = values[:]
                                remove_list = []
                pair.sort(reverse=True)

                if len(pair) == 3:
                        tie_break.append(winning_cards[5:])
                
                
                # Determine hand rank
                # So we can only have pairs here 
                if len(pair) == 1 and not trip:
                        rep = 'pair of ' + self.cn(pair[0]) + 's'
                        # What value do we give a pair in the starting hand?
                        # Scores are out of 1000, a pocket pair will have a base score
                        # of 200?
                        score = 100
                        # We want to add to this score
                        score += sum(winning_cards[:4])
                        tie_break = values[:3]
                elif len(pair) > 1:
                        # We have 2 pair
                        rep = 'two pair -' + self.cn(pair[0]) + 's and ' + self.cn(pair[1]) + 's '
                        score = 200 + sum(winning_cards[:3])
                        tie_break = values[:2]
                elif trip and not pair:
                        rep = 'trip ' + self.cn(trip[0]) + 's '
                        score = 300 + sum(winning_cards[:3])
                        tie_break = values[2:]
                elif straight > 0 and not flush:
                        rep = 'Straight, ' + self.cn(straight)  + ' high'
                        score = 400 + straight # + straight
                elif flush:
                        flush = []
                        for card in hand:
                                if key in card.suit:
                                        flush.append(card.value)
                        flush.sort(reverse=True)
                        rep = 'Flush, ' + self.cn(flush[0]) + ' high'
                        score = 500 + int(flush[0])
                        tie_break = flush[:]
                elif len(trip) == 1 and len(pair) >= 1:
                        rep = 'full house - ' + self.cn(trip[0]) + 's full of ' + self.cn(pair[0]) + 's '
                        score = 600 + sum(winning_cards[:3])
                elif quad:
                        rep = 'four ' + self.cn(quad[0]) + 's '
                        score = 700 + sum(winning_cards[4:])
                        tie_break = values[:1]
                elif straight in range(1,9) and flush:
                        rep = 'Straight flush, ' + self.cn(straight) + ' high'
                        score = 800 + straight
                else:
                        rep = 'high card ' + self.cn(values[0])
                        score = values[0]
                        tie_break = values[:4]
                # Below will screw with the score comparison
                # if flush_score == len(hand):
                #         score += 30 # Small amount
                # if straight_prob:
                #         score += 25  # Small addition
                return score

        # Function to convert values to corresponding names
        def cn(self,value):
                name = self.names[value]  # Convert value to corresponding name
                return str(name)

        def score_values(self,value):
                card_values = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 15, 11: 25, 12: 25, 13: 30}
                return card_values[value]

        def is_straight(self,values):
                hand = values

                if hand[0] == 13:
                        hand.append(0)
                prev = hand[0]
                flag = 1
                for i in range(1,len(hand)):
                        if prev - hand[i] != 1:
                                flag = 0
                                break
                        else:
                                prev = hand[i]
                if len(values) == 5 and flag:
                        return hand[0]
                elif flag and len(values) < 5:
                        return -1
                else:
                        return 0 

##poker player strategy and i/o

import random, pokerhands
from collections import Counter
from operator import attrgetter


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
        RANKS=['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        SUITS=['h', 'c', 's', 'd']
        VALS = {1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'10', 10:'J', 11:'Q', 12:'K', 13: 'A'}
        def decide_play(self, player, pot):

                # So, what we are going to do is evaluate the score of my hand
                # Then generate, lets say 1000 random other hands, and eval their score
                # Then, if my hand is better than a certain percentage
                score, hand_str, tie_break, raw_data = player.get_value()
                # print(f"Jt has {hand_str}")
                # print(f"Jt needs to play {player.to_play}")
                # print(f"He has {player.stack}")                # Now we need to generate a ton of random hands
                table_cards = []
                for card in player.total_cards:
                        if card not in player.cards:
                                table_cards.append(card)
                # Parse the table cards
                table_values = []
                table_suits = []

                for card in table_cards:
                      table_values.append(self.VALS[card.value])
                      table_suits.append(card.suit)
                
                wins = 0
                losses = 0
                for i in range(50000):
                        hand = self.gen_hand(table_values,table_suits)
                        # print(hand)
                        full_vals = table_values + hand[0]
                        full_suits = table_suits + hand[1]

                        hand_score = self.score(full_vals,full_suits)
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
                        to_bet = round(player.stack * 0.2)
                        if to_bet < player.to_play or to_bet < 1:
                                player.check_call(pot)
                        else:
                              player.bet(pot,to_bet)
                elif win_percentage > 0.4:
                        player.check_call(pot)
                else:
                        if player.stack == 0:
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
                card1_val = random.choice(self.RANKS)
                card1_suit = random.choice(self.SUITS)

                card2_val = random.choice(self.RANKS)
                card2_suit = random.choice(self.SUITS)
                return [[card1_val,card2_val],[card1_suit,card2_suit]]
                
        
        # This will generate a score for the given hand
        def score(self,v,suits):
                score = 0
                values = []

                for val in v:
                      values.append(self.RANKS.index(val)+1)
                raw_values = []
                
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
                        # This is casuing errors
                        for val in values:
                              flush.append(val)
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
                
class nickwarren(Strategy):
  #found this data online, very fun to format
  #Name | EV |Win %|Tie %|Occur %|Cumlative %
  dealt_lookup_table = {
    
    'AAo': [0.70, 84.93, 0.54, 0.45, 0.45],
    'KKo': [0.64, 82.11, 0.55, 0.45, 0.90],
    'QQo': [0.59, 79.63, 0.58, 0.45, 1.35],
    'JJo': [0.54, 77.15, 0.63, 0.45, 1.80],
    'TTo': [0.50, 74.66, 0.70, 0.45, 2.26],
    '99o': [0.44, 71.66, 0.78, 0.45, 2.71],
    '88o': [0.38, 68.71, 0.89, 0.45, 3.16],
    'AKs': [0.34, 66.21, 1.65, 0.30, 3.46],
    '77o': [0.32, 65.72, 1.02, 0.45, 3.92],
    'AQs': [0.32, 65.31, 1.79, 0.30, 4.22],
    'AJs': [0.30, 64.39, 1.99, 0.30, 4.52],
    'AKo': [0.30, 64.46, 1.70, 0.90, 5.42],
    'ATs': [0.29, 63.48, 2.22, 0.30, 5.73],
    'AQo': [0.28, 63.50, 1.84, 0.90, 6.63],
    'AJo': [0.27, 62.53, 2.05, 0.90, 7.54],
    'KQs': [0.26, 62.40, 1.98, 0.30, 7.84],
    '66o': [0.26, 62.70, 1.16, 0.45, 8.29],
    'A9s': [0.25, 61.50, 2.54, 0.30, 8.59],
    'ATo': [0.25, 61.56, 2.30, 0.90, 9.50],
    'KJs': [0.25, 61.47, 2.18, 0.30, 9.80],
    'A8s': [0.23, 60.50, 2.87, 0.30, 10.10],
    'KTs': [0.23, 60.58, 2.40, 0.30, 10.40],
    'KQo': [0.22, 60.43, 2.04, 0.90, 11.31],
    'A7s': [0.21, 59.38, 3.19, 0.30, 11.61],
    'A9o': [0.21, 59.44, 2.64, 0.90, 12.51],
    'KJo': [0.21, 59.44, 2.25, 0.90, 13.42],
    '55o': [0.20, 59.64, 1.36, 0.45, 13.87],
    'QJs': [0.20, 59.07, 2.37, 0.30, 14.17],
    'K9s': [0.19, 58.63, 2.70, 0.30, 14.47],
    'A5s': [0.19, 58.06, 3.71, 0.30, 14.78],
    'A6s': [0.19, 58.17, 3.45, 0.30, 15.08],
    'A8o': [0.19, 58.37, 2.99, 0.90, 15.98],
    'KTo': [0.19, 58.49, 2.48, 0.90, 16.89],
    'QTs': [0.18, 58.17, 2.59, 0.30, 17.19],
    'A4s': [0.18, 57.13, 3.79, 0.30, 17.49],
    'A7o': [0.17, 57.16, 3.34, 0.90, 18.40],
    'K8s': [0.16, 56.79, 3.04, 0.30, 18.70],
    'A3s': [0.16, 56.33, 3.77, 0.30, 19.00],
    'QJo': [0.16, 56.90, 2.45, 0.90, 19.90],
    'K9o': [0.15, 56.40, 2.80, 0.90, 20.81],
    'A5o': [0.15, 55.74, 3.90, 0.90, 21.71],
    'A6o': [0.15, 55.87, 3.62, 0.90, 22.62],
    'Q9s': [0.15, 56.22, 2.88, 0.30, 22.92],
    'K7s': [0.15, 55.84, 3.38, 0.30, 23.22],
    'JTs': [0.15, 56.15, 2.74, 0.30, 23.52],
    'A2s': [0.14, 55.50, 3.74, 0.30, 23.83],
    'QTo': [0.14, 55.94, 2.68, 0.90, 24.73],
    '44o': [0.14, 56.25, 1.53, 0.45, 25.18],
    'A4o': [0.13, 54.73, 3.99, 0.90, 26.09],
    'K6s': [0.13, 54.80, 3.67, 0.30, 26.39],
    'K8o': [0.12, 54.43, 3.17, 0.90, 27.30],
    'Q8s': [0.12, 54.41, 3.20, 0.30, 27.60],
    'A3o': [0.11, 53.85, 3.97, 0.90, 28.50],
    'K5s': [0.11, 53.83, 3.91, 0.30, 28.80],
    'J9s': [0.11, 54.11, 3.10, 0.30, 29.11],
    'Q9o': [0.10, 53.86, 2.99, 0.90, 30.01],
    'JTo': [0.10, 53.82, 2.84, 0.90, 30.92],
    'K7o': [0.10, 53.41, 3.54, 0.90, 31.82],
    'A2o': [0.09, 52.94, 3.96, 0.90, 32.73],
    'K4s': [0.09, 52.88, 3.99, 0.30, 33.03],
    'Q7s': [0.08, 52.52, 3.55, 0.30, 33.33],
    'K6o': [0.08, 52.29, 3.85, 0.90, 34.23],
    'K3s': [0.08, 52.07, 3.96, 0.30, 34.53],
    'T9s': [0.08, 52.37, 3.30, 0.30, 34.84],
    'J8s': [0.08, 52.31, 3.40, 0.30, 35.14],
    '33o': [0.07, 52.83, 1.70, 0.45, 35.59],
    'Q6s': [0.07, 51.67, 3.86, 0.30, 35.89],
    'Q8o': [0.07, 51.93, 3.33, 0.90, 36.80],
    'K5o': [0.06, 51.25, 4.12, 0.90, 37.70],
    'J9o': [0.06, 51.63, 3.22, 0.90, 38.61],
    'K2s': [0.06, 51.23, 3.94, 0.30, 38.91],
    'Q5s': [0.05, 50.71, 4.11, 0.30, 39.21],
    'T8s': [0.04, 50.50, 3.65, 0.30, 39.51],
    'K4o': [0.04, 50.22, 4.20, 0.90, 40.42],
    'J7s': [0.04, 50.45, 3.74, 0.30, 40.72],
    'Q4s': [0.03, 49.76, 4.18, 0.30, 41.02],
    'Q7o': [0.03, 49.90, 3.72, 0.90, 41.93],
    'T9o': [0.03, 49.81, 3.43, 0.90, 42.83],
    'J8o': [0.02, 49.71, 3.55, 0.90, 43.74],
    'K3o': [0.02, 49.33, 4.18, 0.90, 44.64],
    'Q6o': [0.02, 48.99, 4.05, 0.90, 45.55],
    'Q3s': [0.02, 48.93, 4.16, 0.30, 45.85],
    '98s': [0.01, 48.85, 3.88, 0.30, 46.15],
    'T7s': [0.01, 48.65, 3.97, 0.30, 46.45],
    'J6s': [0.01, 48.57, 4.06, 0.30, 46.75],
    'K2o': [0.01, 48.42, 4.17, 0.90, 47.66],
    '22o': [0.00, 49.38, 1.89, 0.45, 48.11],
    'Q2s': [0.00, 48.10, 4.13, 0.30, 48.41],
    'Q5o': [0.00, 47.95, 4.32, 0.90, 49.32],
    'J5s': [0.00, 47.82, 4.33, 0.30, 49.62],
    'T8o': [0.00, 47.81, 3.80, 0.90, 50.52],
    'J7o': [0.00, 47.72, 3.91, 0.90, 51.43],
    'Q4o': [-0.01, 46.92, 4.40, 0.90, 52.33],
    '97s': [-0.01, 46.99, 4.25, 0.30, 52.63],
    'J4s': [-0.01, 46.86, 4.40, 0.30, 52.94],
    'T6s': [-0.02, 46.80, 4.28, 0.30, 53.24],
    'J3s': [-0.03, 46.04, 4.37, 0.30, 53.54],
    'Q3o': [-0.03, 46.02, 4.38, 0.90, 54.44],
    '98o': [-0.03, 46.06, 4.05, 0.90, 55.35],
    '87s': [-0.04, 45.68, 4.50, 0.30, 55.65],
    'T7o': [-0.04, 45.82, 4.15, 0.90, 56.56],
    'J6o': [-0.04, 45.71, 4.26, 0.90, 57.46],
    '96s': [-0.05, 45.15, 4.55, 0.30, 57.76],
    'J2s': [-0.05, 45.20, 4.35, 0.30, 58.06],
    'Q2o': [-0.05, 45.10, 4.37, 0.90, 58.97],
    'T5s': [-0.05, 44.93, 4.55, 0.30, 59.27],
    'J5o': [-0.05, 44.90, 4.55, 0.90, 60.18],
    'T4s': [-0.06, 44.20, 4.65, 0.30, 60.48],
    '97o': [-0.07, 44.07, 4.45, 0.90, 61.38],
    '86s': [-0.07, 43.81, 4.84, 0.30, 61.68],
    'J4o': [-0.07, 43.86, 4.63, 0.90, 62.59],
    'T6o': [-0.07, 43.84, 4.48, 0.90, 63.49],
    '95s': [-0.08, 43.31, 4.81, 0.30, 63.80],
    'T3s': [-0.08, 43.37, 4.62, 0.30, 64.10],
    '76s': [-0.09, 42.82, 5.08, 0.30, 64.40],
    'J3o': [-0.09, 42.96, 4.61, 0.90, 65.30],
    '87o': [-0.09, 42.69, 4.71, 0.90, 66.21],
    'T2s': [-0.10, 42.54, 4.59, 0.30, 66.51],
    '85s': [-0.10, 41.99, 5.10, 0.30, 66.81],
    '96o': [-0.11, 42.10, 4.77, 0.90, 67.72],
    'J2o': [-0.11, 42.04, 4.59, 0.90, 68.62],
    'T5o': [-0.11, 41.85, 4.78, 0.90, 69.53],
    '94s': [-0.12, 41.40, 4.90, 0.30, 69.83],
    '75s': [-0.12, 40.97, 5.39, 0.30, 70.13],
    'T4o': [-0.12, 41.05, 4.89, 0.90, 71.04],
    '93s': [-0.13, 40.80, 4.91, 0.30, 71.34],
    '86o': [-0.13, 40.69, 5.08, 0.90, 72.24],
    '65s': [-0.13, 40.34, 5.57, 0.30, 72.54],
    '84s': [-0.14, 40.10, 5.19, 0.30, 72.85],
    '95o': [-0.14, 40.13, 5.06, 0.90, 73.75],
    'T3o': [-0.14, 40.15, 4.87, 0.90, 74.66],
    '92s': [-0.15, 39.97, 4.88, 0.30, 74.96],
    '76o': [-0.15, 39.65, 5.33, 0.90, 75.86],
    '74s': [-0.16, 39.10, 5.48, 0.30, 76.16],
    'T2o': [-0.16, 39.23, 4.85, 0.90, 77.07],
    '54s': [-0.17, 38.53, 5.84, 0.30, 77.37],
    '85o': [-0.17, 38.74, 5.37, 0.90, 78.28],
    '64s': [-0.17, 38.48, 5.70, 0.30, 78.58],
    '83s': [-0.18, 38.28, 5.18, 0.30, 78.88],
    '94o': [-0.18, 38.08, 5.17, 0.90, 79.78],
    '75o': [-0.18, 37.67, 5.67, 0.90, 80.69],
    '82s': [-0.19, 37.67, 5.18, 0.30, 80.99],
    '73s': [-0.19, 37.30, 5.46, 0.30, 81.29],
    '93o': [-0.19, 37.42, 5.18, 0.90, 82.20],
    '65o': [-0.20, 37.01, 5.86, 0.90, 83.10],
    '53s': [-0.20, 36.75, 5.86, 0.30, 83.40],
    '63s': [-0.20, 36.68, 5.69, 0.30, 83.71],
    '84o': [-0.21, 36.70, 5.47, 0.90, 84.61],
    '92o': [-0.21, 36.51, 5.16, 0.90, 85.52],
    '43s': [-0.22, 35.72, 5.82, 0.30, 85.82],
    '74o': [-0.22, 35.66, 5.77, 0.90, 86.72],
    '72s': [-0.23, 35.43, 5.43, 0.30, 87.02],
    '54o': [-0.23, 35.07, 6.16, 0.90, 87.93],
    '64o': [-0.23, 35.00, 6.01, 0.90, 88.83],
    '52s': [-0.24, 34.92, 5.83, 0.30, 89.14],
    '62s': [-0.24, 34.83, 5.66, 0.30, 89.44],
    '83o': [-0.25, 34.74, 5.46, 0.90, 90.34],
    '42s': [-0.26, 33.91, 5.82, 0.30, 90.64],
    '82o': [-0.26, 34.08, 5.48, 0.90, 91.55],
    '73o': [-0.26, 33.61, 5.61, 0.90, 92.45],
    '53o': [-0.27, 33.54, 5.88, 0.90, 93.36],
    '63o': [-0.27, 33.34, 5.87, 0.90, 94.26],
    '32s': [-0.28, 33.09,	5.78,	0.30,	94.57],
    '43o': [-0.28, 32.46, 6.10, 0.90, 95.17],
    '72o': [-0.28, 32.29, 6.00, 0.90, 96.07],
    '52o': [-0.29, 32.09, 6.14, 0.90, 96.98],
    '62o': [-0.29, 31.94, 6.04, 0.90, 97.88],
    '42o': [-0.30, 31.22, 6.16, 0.90, 98.79],
    '32o': [-0.35, 29.23,	6.12,	0.90,	100.00]

}
  max_blind = 20
  class Card:
    RANKS=['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']

    SUITS=['h', 'c', 's', 'd']

    def __init__(self,rank, suit):

      self.rank=rank
      self.suit=suit
      self.value=(nickwarren.Card.RANKS.index(self.rank)+1)

    def __str__(self):
        return str(self.rank)+str(self.suit)


    def __eq__(self, other):
      return self.rank == other.rank and self.suit == other.suit
    

  def simulate(self, player_cards, table_cards):
    sim_deck = self.deck.copy()
    random.shuffle(sim_deck)
    #deal random cards to player
    for i in range(1,len(player_cards)):
      player_cards[i][0] = sim_deck[0]
      sim_deck.pop(0)
      player_cards[i][1] = sim_deck[0]
      sim_deck.pop(0)


    #deal community cards
    while(len(table_cards) < 5):
      table_cards.append(sim_deck.pop(0))

    #get initial
    hand_rating = pokerhands.evaluate_hand(table_cards + player_cards[0])

    #determine if we have high hand in sim game
    for i in range(1,len(player_cards)):
      if hand_rating < pokerhands.evaluate_hand(table_cards + player_cards[i]): return False
    return True
  

  def decide_play(self, player, pot):
    hand_value, rep, tie_break, raw_data=player.get_value()
    raw_values, flush_score, straight, gappers=raw_data
    raw_values.sort()

    
    print("Hand Value: ", hand_value)
    print("Rep: ", rep)
    print("Tie break",tie_break)
    print("Cards ", len(player.total_cards))
    print(raw_data)

    cards_dealt = len(player.total_cards)
    #initalize deck
    self.deck = [nickwarren.Card(rank,suit) for rank in
                 ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] for suit in
                 ['h','d','c','s']]
    t_cards = [nickwarren.Card(card.rank, card.suit) for card in player.total_cards if card not in player.cards]
    my_cards = [nickwarren.Card(card.rank, card.suit) for card in player.cards]

    self.deck = [deck_card for deck_card in self.deck if deck_card not in t_cards + my_cards]

    #append current hand
    p_cards = [my_cards]

    #placeholder cards for other players
    for i in range(0,len(pot.active_players) - 1):
      p_cards.append([self.Card('2','d'), self.Card('2','d')])

    #simulate possible hands against current hand
    win_rate=0
    n = 500
    for i in range(0,n): 
      if self.simulate(p_cards.copy(),t_cards.copy()): win_rate+= 1
    win_rate = win_rate / n
    print(f'Win Rate: {win_rate}')
    given_odds = (1/win_rate) - 1
    print(f'Odds: {given_odds}')

    #calc odds of winning
    #subtract pot from our money in the pot

    #calc odds for the pot
    #cost to enter pot : total to win in pot

    #if offered odds are more than quadruple ours, call

    #when good enough hand, offer only up to our odds of winning?
    #i.e when our odds of winning are 2:1 e.g 66% win rate. We would bet up to %50 of our stack.


    if(cards_dealt == 2): self.pre_flop_strat(player, pot, win_rate)
    if(cards_dealt == 5): self.flop_strat(player,pot, win_rate)
    if(cards_dealt == 6): self.turn_strat(player,pot, win_rate)
    if(cards_dealt == 7): self.river_strat(player, pot, win_rate)
    #standard rules to determine all in or folding
    
    #fold on all in
    

    #print(player.hand)
    #if pair or greater, heuristic is greater
    #calculate using known cards the odds of a hand beating ours. 
      #0-7 cards known, subtract known cards, check possible combinations of unknown cards and strenghth,
        #return number of hands stronger than ours.
        #if greater than some metric, play safe
        #if less than some metric, play aggressive
        #if unbeatable hand, all in
        #if absolutly horrendous hand, fold. (or bluff?)
      #maybe some metric to focus on certain players whom are raising.
        #if raised, start calculating odds
      #never fold if not raised.
      #never fold on pair?

  
    #store all starting pairs, play game using same rules, record outcome W/L per hand.
    #we dont wanna win game, we want to stay above 1000 and win hands.
  def pre_flop_strat(self, player, pot, odds):
    choice = 3

    expected_v, win_rate, tie_rate = self.get_stats(player,pot)
    min_bet, max_bet = self.calc_bet_range(player,pot)

    print('Win Odds: ', odds)
    if(odds > .5): choice = 1
    if(odds < .3 and player.to_play > 0 and not player.all_in): choice = 0
    if(player.to_play >= player.stack - player.in_pot and odds < .7 and not player.all_in): choice = 0

    #standard rules to determine all in or folding
    if(choice != 0 and player.to_play > expected_v * player.stack): choice = 1
    #fold on all in
    #if(win_rate < 60 and player.to_play >= max_bet and not player.all_in): choice = 0
    #all in if cannot afford next round
    if(player.stack <= pot.blinds[1]*2): choice = 2

    if(player.to_play == 2 and choice == 0): choice = 3

    if choice==0: #fold
      player.fold(pot)
    elif choice==1: #call
      if player.stack<=player.to_play or player.raised:
        player.check_call(pot)
      else:
        max_bet_ev = (int(abs(expected_v) * max_bet) // 10) * 10
        print(max_bet_ev)
        player.bet(pot, max_bet_ev)
    elif choice==2: #all in
      if player.stack<=player.to_play:
        player.check_call(pot)
      else:
        player.bet(pot, player.stack)
    else:
      player.check_call(pot)
    #Use lookup table to make play.



  def flop_strat(self, player, pot, odds):
    hand_value, rep, tie_break, raw_data=player.get_value()
    choice = 1

    expected_v, win_rate, tie_rate = self.get_stats(player,pot)
    min_bet, max_bet = self.calc_bet_range(player,pot)
    print(f'Win Odds {odds}')
    #standard rules to determine all in or folding
    if(player.to_play > expected_v * player.stack): choice = 1
    #fold on all in
    if(win_rate < 60 and player.to_play >= max_bet and not player.all_in): choice = 0
    #all in if cannot afford next round
    if(player.stack <= pot.blinds[1]*2): choice = 2

    if(player.to_play == 2 and choice == 0): choice = 3

    if choice==0: #fold
      player.fold(pot)
    elif choice==1: #call
      if player.stack<=player.to_play or player.raised:
        player.check_call(pot)
      else:
        max_bet_ev = (int(abs(expected_v) * max_bet) // 10) * 10
        print(max_bet_ev)
        player.bet(pot, max_bet_ev)
    elif choice==2: #all in
      if player.stack<=player.to_play:
        player.check_call(pot)
      else:
        player.bet(pot, player.stack)
    else:
      player.check_call(pot)



  def turn_strat(self, player, pot, odds):
    hand_value, rep, tie_break, raw_data=player.get_value()
    choice = 1

    expected_v, win_rate, tie_rate = self.get_stats(player,pot)
    min_bet, max_bet = self.calc_bet_range(player,pot)

    print(f'Win Odds {odds}')

    #standard rules to determine all in or folding
    if(player.to_play > expected_v * player.stack): choice = 1
    #fold on all in
    if(win_rate < 60 and player.to_play >= max_bet and not player.all_in): choice = 0
    #all in if cannot afford next round
    if(player.stack <= pot.blinds[1]*2): choice = 2

    if(player.to_play == 0 and choice == 0): choice = 3

    #hand value
    if choice==0: #fold
      player.fold(pot)
    elif choice==1: #call
      if player.stack<=player.to_play or player.raised:
        player.check_call(pot)
      else:
        max_bet_ev = (int(abs(expected_v) * max_bet) // 10) * 10
        print(max_bet_ev)
        player.bet(pot, max_bet_ev)
    elif choice==2: #all in
      if player.stack<=player.to_play:
        player.check_call(pot)
      else:
        player.bet(pot, player.stack)
    else:
      player.check_call(pot)




  def river_strat(self, player, pot, odds):
    hand_value, rep, tie_break, raw_data=player.get_value()
    choice = 1

    expected_v, win_rate, tie_rate = self.get_stats(player,pot)
    min_bet, max_bet = self.calc_bet_range(player,pot)

    print(f'Win Odds {odds}')

    #standard rules to determine all in or folding
    if(player.to_play > expected_v * player.stack): choice = 1
    #fold on all in
    if(win_rate < 60 and player.to_play >= max_bet and not player.all_in): choice = 0
    #all in if cannot afford next round
    if(player.stack <= pot.blinds[1]*2): choice = 2

    if(player.to_play == 2 and choice == 0): choice = 3

    if choice==0: #fold
      player.fold(pot)
    elif choice==1: #call
      if player.stack<=player.to_play or player.raised:
        player.check_call(pot)
      else:
        max_bet_ev = (int(abs(expected_v) * max_bet) // 10) * 10
        print(max_bet_ev)
        player.bet(pot, max_bet_ev)
    elif choice==2: #all in
      if player.stack<=player.to_play:
        player.check_call(pot)
      else:
        player.bet(pot, player.stack)
    else:
      player.check_call(pot)





  def calc_bet_range(self, player, pot):
    max_bet = player.stack - player.to_play
    min_bet = player.to_play
    if max_bet<min_bet:
        min_bet = max_bet 


    if max_bet<0:
      max_bet=player.stack
      min_bet=max_bet
    
    print('max bet '+str(max_bet))
    print('min be  '+str(min_bet))
         

    return min_bet, max_bet

  def get_stats(self, player, pot):
    hand_raw = player.cards
    hand = ""
    if(hand_raw[0].value > hand_raw[1].value):
      if(hand_raw[0].suit == hand_raw[1].suit and not hand_raw[0].value == hand_raw[1].value):
        hand = hand_raw[0].rank + hand_raw[1].rank + 's'
      else:
        hand = hand_raw[0].rank + hand_raw[1].rank + 'o'
    else:
      if(hand_raw[0].suit == hand_raw[1].suit and not hand_raw[0].value == hand_raw[1].value):
        hand = hand_raw[1].rank + hand_raw[0].rank + 's'
      else:
        hand = hand_raw[1].rank + hand_raw[0].rank + 'o'
    hand = hand.replace('10','T')
    print(hand)

    stats = self.dealt_lookup_table[hand]
    
    expected_v = stats[0]
    win_rate = stats[1]
    tie_rate = stats[2]
    print(expected_v, win_rate, tie_rate)
    return expected_v, win_rate, tie_rate

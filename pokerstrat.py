##poker player strategy and i/o

import random, pokerhands

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

        
                                
class Test(Strategy):
        options=[['x', 'f', 'b'], ['c', 'r', 'f'], ['c', 'f']]
        choices={0:'check, fold or bet', 1:'call, raise, fold', 2:'call all-in or fold'}

        table_info = [] # This will hold information ertaining to the table. Previous pot, etc.

        def decide_play(self, player, pot):
                # So What do we do here!
                # Rep = Represents hand rank, not sure if useful!
                # Hand value = Text representation of thing
                # Raw Data =
                rep, hand_value, tie_break, raw_data = player.get_value()
                # Testing out what each thing here is
                # The SklanskySys2 only utilizes rep and raw_data, so lets see what that is
                print(f"Rep: {rep}")
                print(f"Hand value: {hand_value}")
                print(f"Raw Data: {raw_data}")
                useable_cards = raw_data[0] # Grabs the useable card values
                # Determine length of hand, what our hand has, and go from there
                if len(useable_cards) == 2:
                        # if we're in the starting hand, determine what we can do
                        can_check = 1
                        if player.to_play != 0:
                                can_check = 0
                        decision = self.first_hand(player, raw_data, can_check, pot)
                        # Use decision to make first move
                        if decision[0] == 0:
                                player.check_call(pot)
                        elif decision[0] == 1:
                                player.bet(pot,decision[1])
                        else:
                                player.fold(pot)
                else:
                        options=Test.options
                        choices=Test.choices
                        action=''
                        op=0


                        if player.to_play==0:
                                op=0
                        elif player.to_play<player.stack:
                                op=1
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

        # TODO: Figure out what these will do
        def first_hand(self, player, raw_data, can_check, pot):
                percentage = 0
                # Break up the raw_data
                hand = raw_data[0] # This is all we need

                # For the starting hand, all we really wanna determine
                # is whether or not there is a pair
                is_pair = 0
                if hand[0] == hand[1]:
                        is_pair = 1
                
                # If we have a pocket pair we instantly want to bet, not too much though
                if is_pair:
                        # Idk why spacing is so weird
                        if hand[0] >= 10:
                                percentage += 0.05
                        elif hand[0] < 10 and hand[0] >=7:
                                percentage += 0.025
                if percentage > 0:
                        # We want to bet
                        bet_amount = self.to_bet(player,percentage)
                        if can_check:
                                return [1,bet_amount]
                        else:
                                needed_bet = player.to_play
                                if needed_bet < bet_amount:
                                        # Raise
                                        return [1,bet_amount]
                                elif needed_bet - bet_amount > 300:
                                        # Fold
                                        return [-1,0]
                                else:
                                        # Call
                                        return [0,0]
                else:
                        # try to check
                        if can_check:
                                return [0,0]
                        else:
                                # If we cant check we need to compare our hand against
                                # Whatever the current bet is
                                if (hand[0] > 7 or hand[1] > 7) and player.to_play < player.stack * 0.2:
                                        # Call
                                        return [0,0]
                                else:
                                        # Fold
                                        return [-1,0]



        # Return numeric amount to bet
        def to_bet(self, player, percentage):
                return player.stack * percentage
                
            
            
		
			
			
			
			
		
	
	
	

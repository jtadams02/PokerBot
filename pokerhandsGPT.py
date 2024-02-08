# Pokerhand evaluator

# Dictionary for value:name conversion
names = {1:'deuce', 2:'three', 3:'four', 4:'five', 5:'six', 6:'seven', 7:'eight', 8:'nine', 9:'ten', 10:'jack', 11:'queen', 12:'king', 13:'ace'}

# Importing necessary modules
from collections import Counter
from operator import attrgetter

# Function to convert values to corresponding names
def cn(value):
    name = names[value]  # Convert value to corresponding name
    return str(name)

# Function to check for a straight
def is_straight(values, length):
    hand = set(values)  # Create a set of unique values in the hand
    if 13 in hand:  # If ace is present
        hand.add(0)  # Add 0 as another possible value for ace (to handle A, 2, 3, 4, 5 straight)
    
    # Check for straight starting from highest possible value
    for low in (10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        needed = set(range(low, low + length))  # Create a set of values needed for a straight
        if len(needed - hand) <= 0:  # If all needed values are present in the hand
            return (low + length) - 1  # Return the highest value of the straight
    
    return 0  # If no straight is found

# Function to evaluate a poker hand
def evaluate_hand(cards):
    # Split cards into values and suits
    values = []
    raw_values = []
    suits = []
    flush = False
    high_card = True  # Flag for high card
    
    # Extract values and suits from each card
    for card in cards:
        values.append(card.value)  # Append the value of the card to values list
        suits.append(card.suit)    # Append the suit of the card to suits list
    
    # Keep raw data on values
    raw_values = values[:]  # Copy values to raw_values
    
    # Perform histogram on values and suits
    value_count = Counter(values)  # Count occurrences of each value
    suit_count = Counter(suits)    # Count occurrences of each suit
    
    # Put values in order of rank
    values.sort(reverse=True)  # Sort values in descending order
    
    # Set up variables
    pair_l = []
    trip_l = []
    quad_l = []
    multiples_l = [0, 0, pair_l, trip_l, quad_l]  # List to store pairs, trips, quads
    remove_list = []  # List of multiples to be removed
    rep = ''           # Variable to represent hand rank
    hand_value = 0     # Variable to represent hand value
    tie_break = 0      # Variable for tie-breaking
    winning_cards = [] # List to store winning cards
    
    limit = len(values)
    if limit > 5:
        limit = 5  # Limit to 5 cards for evaluation
    
    straight = is_straight(values, limit)  # Check for straight
    
    # Iterate through values
    for key, value in value_count.items():
        # If histogram is more than one, it's pair, trip or quads
        if value > 1:
            high_card = False  # Set high_card flag to False
            multiples_l[value].append(key)  # Append key to corresponding list based on count
            for element in values:
                if element == key:
                    remove_list.append(element)  # Append element to remove_list
                    winning_cards.append(element)  # Append element to winning_cards
            
            # Remove elements from values list
            for item in remove_list:
                values.remove(item)
            
            winning_cards.sort(reverse=True)  # Sort winning_cards in descending order
            tie_break = values[:]  # Set tie_break to remaining values
            remove_list = []  # Clear remove_list for next iteration
    
    pair_l.sort(reverse=True)  # Sort pair list in descending order
    
    # Avoid having three pairs
    if len(pair_l) == 3:
        tie_break.append(winning_cards[5:])  # Append extra cards to tie_break
    
    # Check for flush
    for key, value in suit_count.items():
        flush_score = 0
        if value == 5:
            flush = True  # Set flush flag to True
            high_card = False  # Set high_card flag to False
        else:
            flush_score = value  # Update flush_score
    
    # Determine hand rank
    if len(pair_l) == 1 and not trip_l:
        rep = 'pair of ' + cn(pair_l[0]) + 's'
        hand_value = 100 + (sum(winning_cards[:2]))  # Calculate hand value
        tie_break = values[:3]  # Update tie_break
    # Code continues...
    # Continued from previous code snippet...

    elif len(pair_l) > 1:
        rep = 'two pair - ' + cn(pair_l[0]) + 's and ' + cn(pair_l[1]) + 's '
        hand_value = 200 + (sum(winning_cards[:4]))  # Calculate hand value
        tie_break = values[:1]  # Update tie_break
    
    elif trip_l and not pair_l:
        rep = 'trip ' + cn(trip_l[0]) + 's '
        hand_value = 300 + (sum(winning_cards[:3]))  # Calculate hand value
        tie_break = values[:2]  # Update tie_break
    
    elif straight > 0 and not flush:
        rep = 'Straight, ' + cn(straight) + ' high'
        hand_value = 400 + straight  # Calculate hand value
    
    elif flush:
        flush_l = []
        for card in cards:
            if key in card.suit:
                flush_l.append(card.value)  # Append value of flush cards
        flush_l.sort(reverse=True)  # Sort flush cards in descending order
        rep = 'Flush, ' + cn(flush_l[0]) + ' high'
        hand_value = 500 + int(flush_l[0])  # Calculate hand value
        tie_break = flush_l[:]  # Update tie_break
    
    elif len(trip_l) == 1 and len(pair_l) >= 1:
        rep = 'full house - ' + cn(trip_l[0]) + 's full of ' + cn(pair_l[0]) + 's'
        hand_value = 600 + (sum(winning_cards[:3]))  # Calculate hand value
    
    elif quad_l:
        rep = 'four ' + cn(quad_l[0]) + ' s'
        hand_value = 700 + (sum(winning_cards[:4]))  # Calculate hand value
        tie_break = values[:1]  # Update tie_break
    
    elif straight in range(1, 9) and flush:
        rep = 'Straight flush, ' + cn(straight) + ' high'
        hand_value = 800 + straight  # Calculate hand value

    # If high_card is true:
    else:
        rep = 'high card ' + cn(values[0])
        hand_value = values[0]  # Set hand value to highest card value
        tie_break = values[:4]  # Update tie_break
    
    # Calculate gappers
    gappers = (raw_values[0]) - (raw_values[1])
    raw_data = (raw_values, flush_score, straight, gappers)  # Store raw data
    
    return rep, hand_value, tie_break, raw_data  # Return hand evaluation results

'''
Elena Corpus
CSCI 160
Tuesday 5:00 - 7:00 pm
program that will ask you to enter Ace, Jack, Queen, King
'''

points_total = 0
points_king = 0
points_jack = 0
points_queen = 0
points_ace = 0

total_king = 0
total_jack = 0
total_queen = 0
total_ace = 0
total_cards = 0

ave_queen = 0
ave_ace = 0

card_name = str(input("Enter a card from Ace or Jack or Queen or King: "))
card_points = int(input("Enter the points on the card: "))

while card_points != 0:
    
    if card_name == "Ace": 
        total_ace = total_ace + 1
        points_ace = (card_points * 1) + points_ace

    elif card_name == "Jack":
        total_jack = total_jack + 1
        points_jack = (card_points * 11) + points_jack 
        
    elif card_name == "Queen":
        total_queen = total_queen + 1
        points_queen = (card_points * 12) + points_queen

    elif card_name == "King":
        total_king = total_king + 1
        points_king = (card_points * 13) + points_king
         
    total_cards = total_king + total_queen + total_ace + total_jack
    points_total = points_ace + points_jack + points_king + points_queen

    card_name = str(input("Enter a card from Ace or Jack or Queen or King: "))
    card_points = int(input("Enter the points on the card: "))

print()

print("The total points gained by the user: ", points_total)
print("The sum of counts of all cards:      ", total_cards)

if (total_ace > total_jack) and (total_ace != 0):
    ave_ace = points_ace / total_ace
    print("The average of ace cards:        ", format(ave_ace, '.3f'))
else:    
    print("The number of ace cards are less than the number of jack cards")


if (total_queen > total_king) and (total_queen != 0):
    ave_queen = points_queen / total_queen
    print("The average of queen cards:      ", format(ave_queen,'.2f'))
else:
    print("error")


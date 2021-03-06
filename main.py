from replit import clear
from art import logo
import random

############### Blackjack Project #####################

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def deal_new_card(list,is_player=False):
    card = random.choice(cards)
    if is_player:
        list_length=len(list)
        if list_length==1:
            print(f" and {card}")
        else:
            if list_length==0:
                print(f"You drew {card}",end="")
            else:
                print(f"You drew {card}")
    if card == 'A':
        if 11 in list:
            list.append(1)
            sum_list = sum(list)
            if sum_list > 21:
                print("You drew ace again, and got over 21, so your previous ace has also been converted to 1")
                list.remove(11)
                list.append(1)
        else:
            sum_list = sum(list)
            if (sum_list+11)>21:
                print("You drew an ace but converted to 1")
                list.append(1)
            else:
                list.append(11)
    elif card =='J' or card=='Q' or card =='K':
        list.append(10)
    else:
        list.append(card)


def blackjack():
    clear()
    print(logo)

    def check_winner():
        print(f"your hand = {player_hand} and total = {sum_player}\npc hand = {pc_hand} and total = {sum_pc}\n")

        if sum_player >21:
            print("You bust")
        elif sum_pc >21:
            print("Dealer bust, you win")
        elif sum_player > sum_pc:
            print("You win")
        elif sum_player == sum_pc:
            print("IT is a draw")
        else:
            print("You lose")

    player_hand =[]
    pc_hand = []
    for i in range(2):
        deal_new_card(player_hand,True)
        deal_new_card(pc_hand)
        sum_pc = sum(pc_hand)
        sum_player=sum(player_hand)
    print(f"Your hand : {player_hand} and total = {sum_player}\nPc hand : {pc_hand[0]}")
    game_over = False

    while sum_player < 22 and not game_over:
        while sum_pc < 17:
            deal_new_card(pc_hand)
            sum_pc=sum(pc_hand)

        hit = input("Do you want to hit or stand\nh = hit\ns = stand\n")
        
        if hit == "h":
            deal_new_card(player_hand,True)
            sum_player=sum(player_hand)
            print(f"your hand = {player_hand} and total = {sum_player}\n")
            if sum_player>21:
                print("You busted")
        else:
            sum_pc = sum(pc_hand)
            sum_player=sum(player_hand)
            check_winner()
            game_over=True
            break

    playing = input("Play again ?\ny=yes\nn=no\n")
    if playing=="y":
        blackjack()
    else:
        clear()

blackjack()
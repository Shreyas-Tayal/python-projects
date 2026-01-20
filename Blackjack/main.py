from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_mode = True
while game_mode:
    playing = input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no.").lower()
    if playing == "y":
        print("\n"*100 + logo)                          #clearing the screen and displaying the logo


        users_cards = [random.choice(cards),random.choice(cards)]
        users_total = 0
        for x in users_cards:
            users_total += x
        print(f"Your cards are {users_cards} and your current total is {users_total}.")

        dealers_first_card = (random.choice(cards))
        dealers_cards = [dealers_first_card,random.choice(cards)]
        dealers_total = 0
        for x in  dealers_cards:
            dealers_total += x

        playing_user = True                             #tracks whether the user has passed or not
        playing_dealer = True                           #tracks whether the dealer has passed or not
        game = True
        blackjack_counter = 0

        while playing_user and playing_dealer and game:          #the start of another round
            print(f"The dealer's first card is {dealers_first_card}.")
            hit_or_pass = input("Enter 'y' to hit/draw another card or enter 'n' to pass.\n\n").lower()
            if hit_or_pass == "y":
                extra_card = random.choice(cards)
                users_cards.append(extra_card)
                users_total += extra_card
                print(f"Your cards are {users_cards} and your current total is {users_total}.")
                print(f"The dealer's first card is {dealers_first_card}.")

                if users_total > 21:
                    print("You went over 21. YOU LOSE!!!")
                    print(f"Your final hand: {users_cards}, your final total: {users_total}")
                    print(f"The dealer's final hand: {dealers_cards}, dealer's final total: {dealers_total}")
                    game = False

                elif users_total == 21:
                    blackjack_counter += 1              #if the dealer also gets a blackjack, it might be a draw
                    print("You got a BLACKJACK!")
                    print(f"Your hand: {users_cards}, your total: {users_total}")
                    game = False

                else:
                    print(f"Your hand: {users_cards}, your total: {users_total}")

            elif hit_or_pass == "n":
                playing_user = False

            if dealers_total < 17 and users_total < 21:
                extra_card = random.choice(cards)
                dealers_cards.append(extra_card)
                dealers_total += extra_card

                if dealers_total > 21:
                    print("The dealer went over 21. YOU WIN!!!")
                    print(f"Your final hand: {users_cards}, your final total: {users_total}")
                    print(f"The dealer's final hand: {dealers_cards}, dealer's final total: {dealers_total}")
                    game = False

                elif dealers_total == 21:
                    blackjack_counter += 1
                    print("The dealer got a BLACKJACK!")
                    game = False

                elif dealers_total > 16:
                    playing_dealer = False

            else:
                playing_dealer = False


        if users_total > dealers_total and game:
            print("You WIN!!!")
        elif dealers_total > users_total and game:
            print("You LOSE!!!")

        if blackjack_counter == 2:
            print("Both you and the dealer got a BLACKJACK, so it is a draw.")
        if blackjack_counter == 1:
            if users_total == 21:
                print("You WIN!!!")
            else:
                print("You LOSE!!!")

    else:
        game_mode = False




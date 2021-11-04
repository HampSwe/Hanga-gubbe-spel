import os
import random
import image

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

def clear():
    os.system("cls")
    print("--- Hänga Gubbe ---")
    print()

def get_word():
    words = ["hej", "katt", "matematik", "halloween"]
    return random.choice(words).upper()

def game():
    clear()
    
    word = get_word()

    word_as_list = []

    known_as_list = []

    wrong = 0
    max_wrongs = 11
    won = False

    for character in word:
        word_as_list.append(character)
        known_as_list.append("_")

    guessed = ""

    loop = True

    while loop:
        clear()

        if wrong > 0:
            to_print = image.hangman[wrong - 1]

            for i in to_print:
                print(i)

            print("")

        for character in known_as_list:
            print(character, end=" ")

        print()
        print()

        if guessed != "":
            print("Gissade bokstäver:", end=" ")

            for character in guessed:
                print(character, end=" ")
            print()

            if wrong == 0:
                print()
        
        if wrong > 0:
            print("Antal fel: " + str(wrong))
            print("")

        guess = input("Gissa en bokstav! ").upper()
        print()

        if guess in alphabet:
            
            if guess in guessed:
                print("Den bokstaven har du redan gissat på!")
                print()
                input("Tryck på ENTER för att fortsätta ")

            else:
                guessed += guess

                if guess in word_as_list:
                    for i in range(len(word_as_list)):
                        if guess == word_as_list[i]:
                            known_as_list[i] = guess

                    if word_as_list == known_as_list:
                        won = True
                        loop = False

                else:
                    wrong += 1

                    if wrong >= max_wrongs:
                        won = False
                        loop = False
        
        else:
            print("Det där är ingen bokstav i det svenska alfabetet!")
            print()
            input("Tryck på ENTER för att fortsätta ")
    
    clear()

    if won:
        print("Grattis, du har gissat rätt!")
        print("")
        print("Ordet var " + word + "!")

        print("Du klarade det på " + str(wrong) + " av " + str(max_wrongs) + " försök!")

        print()
        input("Tryck på ENTER för att fortsätta ")

    else:
        to_print = image.hangman[len(image.hangman) - 1]
        for i in to_print:
            print(i)
        print("")

        print("Tyvärr, du förlorade!")
        print("")
        print("Ordet var " + word + "!")
                
        print()
        input("Tryck på ENTER för att fortsätta ")
    
    print("")


def intro():

    clear()

    loop = True
    played_again = False

    while loop:
        clear()

        if played_again:
            answer = input("Vill du spela igen? (y/n) ")
        else:
            answer = input("Vill du spela? (y/n) ")

        if answer == "y":
            game()
            played_again = True

        elif answer == "n":
            loop = False

        else:
            clear()
            print("Det där var inte ett giltigt svar!")
            print("")

intro()


# ATT FÖRBÄTTRA

# Gör lower-case
# Fixa en lista med ord
# Gör så att inte funktionerna länkar till varandra
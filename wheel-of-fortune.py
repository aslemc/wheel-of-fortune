import random

from threading import Timer

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

round_num = 0
dictionary = []
turntext = ""
wheellist = []
word = ""
guessed = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""

# functions to read files
def read_dictionary():
    global dictionary
    dictionary_file = open('wheel-txt-files/dictionary.txt')
    dictionary = dictionary_file.readlines()
    dictionary_file.close()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i].replace('\n','')

def read_wheel():
    global wheellist
    wheel_file = open('wheel-txt-files/wheeldata.txt')
    wheellist = wheel_file.readlines()
    wheel_file.close()
    for i in range(len(wheellist)):
        wheellist[i] = wheellist[i].replace('\n','')



# functions for game

# will display round total
def display_scores():
    for i in players:
        print(f"""
        {players[i]['name']}: 
        Game total: ${players[i]['gametotal']}
        Round total: ${players[i]['roundtotal']}""")

#selects the word and creates a list of underscores to represent the current guesses
def get_word():
    global dictionary
    global word
    global guessed
    word = random.choice(dictionary)
    guessed = list('_'*len(word))
    return word, guessed

# sets up the player names and the bank totals (all 0)
def game_setup():
    global players
    global dictionary
    global wheellist
    for i in players:
        name = input(f"Enter the name of Player {i+1}: ")
        players[i] = {"roundtotal":0, "gametotal":0, "name":name}
    read_dictionary()
    read_wheel()

# selects the first player randomly and calls the get_word() function
def round_setup():
    global players
    global word
    global guessed
    get_word()
    first_player = random.randint(1,3)
    print(f"The first player will be player {players[first_player-1]['name']}.")
    return first_player

# allows the player to guess a letter
def guess_letter(letter):
    count = 0
    # check if the letter is in the word. if yes, insert it into the list with the guessed word, count the number of time it occurs,
    # print it out, & continue playing. If not, stop the player's turn.
    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                guessed[i] = letter
                count = count + 1
        print(''.join(guessed))
        if ''.join(guessed) == word:
            print("You guessed it!")
            is_turn = False
        else: 
            is_turn = True
            print("Good guess!")
    else:
        is_turn = False
    return count, is_turn

# allows the player to buy a vowel
def buy_vowel(player_num):
    is_valid = False
    # ensure that the player inputs a vowel
    while not is_valid:
        vowel = input("Guess a vowel: ")
        if vowel in vowels:
            is_valid = True
        else:
            print("That's not a vowel. Try again.")
    # subtract 250
    players[player_num]['roundtotal'] = players[player_num]['roundtotal'] - 250
    # check if the letter is in the word
    is_turn = guess_letter(vowel)[1]
    return is_turn
    

# allows the player to spin the wheel
def spin_wheel(player_num):
    # spin the wheel
    wheel = random.choice(wheellist)
    print(wheel)
    # end turn if the wheel value is bankrupt
    if wheel == 'bankrupt':
        print("BANKRUPT! Your turn is over.")
        players[player_num]['roundtotal'] = 0
        is_turn = False
        return is_turn
    # end turn if the wheel value is lose a turn
    elif wheel == 'lose a turn':
        print("LOSE A TURN! Your turn is over.")
        is_turn = False
        return is_turn
    # if the wheel lands on a number, prompt the player to guess a letter & call guess_letter(). a correct guess
    # continues the player's turn while an incorrect guess ends it.
    elif wheel.isnumeric():
        print(f'You landed on ${wheel}!')
        is_valid = False
        while not is_valid:
            letter = input("Guess a letter: ").lower()
            # checks that the letter is a valid guess 
            if letter in guessed:                    
                print("you've already guessed that one. try again.")
            elif letter in vowels:
                print("that's a vowel. you have to pay for those.")
            elif letter.isalpha() and len(letter) == 1:
                is_valid = True                
            else:
                print("That is not a valid guess. Try again.")
        (count, is_turn) = guess_letter(letter)
        if is_turn:
            players[player_num]['roundtotal'] = players[player_num]['roundtotal'] + (int(wheel)*count)
            print(f"Good job, {players[player_num]['name']}. You now have ${players[player_num]['roundtotal']}!")
            return is_turn
        else:
            print("Sorry, that's not in the word. Your turn is over.")
            return is_turn

# allows the player to guess the full word
def guess_word(player_num):
    guessed_word = input("Guess the word: ").lower()
    if guessed_word == word:
        for i, l in enumerate(word):
            guessed[i] = l
        print("You guessed it!")
        print(''.join(guessed))
    else: 
        is_turn = False
        print("Sorry, that was incorrect!")
    is_turn = False
    return is_turn

# the turn function continues as long as the player does not guess incorrectly or spin badly
def turn(player_num):
    is_turn = True
    print(f"It's {players[player_num]['name']}'s turn! You have ${players[player_num]['roundtotal']}.")
    while is_turn:
        # print out current progress, the options, and let the player choose what to do
        print(f"Current progress: {''.join(guessed)} ({len(word)} letters)")
        print("""
        Options
        ========
        1. Buy a vowel
        2. Spin the wheel
        3. Guess the word""")
        turn = int(input("Enter 1, 2, or 3: "))
        if turn == 1:
            if players[player_num]['roundtotal'] < 250:
                print("Sorry, you don't have enough money to buy a vowel. Choose something else.")
            else:
                is_turn = buy_vowel(player_num)
        if turn == 2:
            is_turn = spin_wheel(player_num)
        if turn == 3:
            is_turn = guess_word(player_num)
    return player_num

# executes round 1 or 2
def round():
    global players
    global word
    global guessed
    first_player = round_setup()-1
    player_num = turn(first_player)
    while word != ''.join(guessed):
        if player_num == 2:
            player_num = turn(0)
        else:
            player_num = turn(player_num+1)
    print(f"And the final word is ")
    print(f"The winner of the round is {players[player_num]['name']}!")
    print("Let's see the current scores.")
    display_scores()
    print(f"Congratulations, {players[player_num]['name']}! You get to keep your winnings for this round.")
    # set all round totals to zero & add winner's round total to their total amount
    for i in players:
        if i == player_num:
            players[i]['gametotal'] = players[i]['gametotal'] + players[i]['roundtotal']
            players[i]['roundtotal'] = 0
        else:
            players[i]['roundtotal'] = 0
    
def final_round():
    global word
    global guessed

    # find player with the most money
    game_totals = [players[i]['gametotal'] for i in players]
    # assign the player with the most money to play this round
    player_num = game_totals.index(max(game_totals))
    print(f"Welcome to the final round! {players[player_num]['name']} will be trying to win the grand prize!")
    print("We will give you one final word to guess. This word will have several letters already filled in.")
    print("You get to guess 3 more consonants and one more vowel, for free.")
    print("After those guesses, you have five seconds to guess the word and win the grand prize!")
    (word, guessed) = get_word()
    # fill in r, s, t, l, n, e
    guess_letter('r')
    guess_letter('s')
    guess_letter('t')
    guess_letter('l')
    guess_letter('n')
    guess_letter('e')
    print(f"Here's your word: {''.join(guessed)} ({len(word)} letters)")
    while ''.join(guessed) != word:
        consonant = 0
        while consonant < 3:
            letter = input("Guess a consonant: ")
            guess_letter(letter)
            consonant = consonant + 1
        letter = input("Guess a vowel: ")
        guess_letter(letter)
        break
    if ''.join(guessed) != word:
        print(f"Here's your chance to guess the final word. You'll have five seconds.")
        timeout = 5
        t = Timer(timeout, print, ['Sorry, times up!'])
        t.start()
        prompt = f"You have %d seconds to answer the question. What is this word?\n{''.join(guessed)}\n" % timeout
        answer = input(prompt)
        t.cancel()
        if answer != word:
            print("Sorry, you lost!")
        else:
            players[player_num]['gametotal'] = players[player_num]['gametotal']+1000
            print(f"Congratulations, you won an extra $1000! You won ${players[player_num]['gametotal']} total!")
    else:
        players[player_num]['gametotal'] = players[player_num]['gametotal']+1000
        print(f"Congratulations, you won an extra $1000! You won ${players[player_num]['gametotal']} total!")

def game():
    game_setup()
    for i in range(0,3):
        if i in [0,1]:
            round()
        else:
            final_round()
    print("Thanks for playing!")

again = 'y'
while again == 'y':
    game()
    again = input("Would you like to play again? Press y to play again: ")
print("Goodbye!")
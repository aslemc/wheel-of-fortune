# 
# 
# players = {player#, {bank, roundbank, name}} x 3
# 
# round_num = 0
# dictionary = text file
# word = 'none'
# guessed = []
# 
# 
# 
# functions
# # ################
#
#
# def get_word()
#   word = random.choice(dictionary)
#   guessed = list('_ '*len(word))
#   
# def player_setup(player_num)
#   for i in players[]
#       name = input(f"Enter the name of player{player_num}: ")
#       players[player_num] = {0, 0, name}
#
# def round_setup()
#   get_word()
#   first_player = random number between 0-2
#   return first_player
#   
# #
# def guess_letter (letter, player_num)
#   if letter in word
#       use the for loop from the word guessing game to display the word
#           include a counter "count"
#       print "good guess"
#       return still_playing, count
#   else
#       print "sorry, that's not in this word" 
#       end turn
# 
# #
# def buy_vowel(player_num)
#   is_valid = False
#   while not is_valid
#       vowel = input("which vowel would you like to guess ")
#       if vowel in vowel_list
#           is_valid = True
#       else:
#           print("That's not a vowel.")
#   -250 from round bank
#    guess_letter(vowel, player_num)
# 
#
# def spin_wheel(player_num)
#   wheel = random value from the wheel values
#   if wheel == bankrupt
#       print("BANKRUPT! Your turn is over.")
#       set player_num's round bank to bankrupt
#       end turn
#   if wheel == lose a turn
#       print("LOSE A TURN! Your turn is over.")
#       end turn
#   if wheel.isnumeric()
#       print(f'You landed on ${wheel}!')
#       is_valid = False
#           while not is_valid:
#               letter = input("Guess a letter: ")
#               if letter in guessed
#                   print("you've already guessed that one. try again.")
#               elif letter in vowel_list
#                   print("that's a vowel. you have to pay for those.")
#               elif letter.isalpha() and len(letter) == 1
#                   is_valid = True
#               else:
#                   "That is not a valid guess. Try again."
#       guess_letter(letter, player_num)
#       if still_playing
#           add wheel*count to round bank
#           return is_turn
#       else
#           end turn
#
# def guess_word(player_num):
#   guessed_word = input("Guess the word: ")
#   if guessed_word == word
#       for i, l in enumerate(word)
#           guessed[i] = ''.join.f'l'
#       print("You guessed it!")
#       
# def turn(player_num)
#   is_turn = True
#   while is_turn
#       turn = input(1, 2, or 3)
#       if turn = 1
#           if player's roundbank < 250
#               print("Sorry, you don't have enough money to buy a vowel")
#           else
#               buy_vowel()
#       if turn = 2
#           spin_wheel()
#       if turn = 3
#           guess_word()
#   return player_num
# 
# def cash_out()
#   for i in players.keys()
#       add roundbank to bank if roundbank is max
# 
# def print_score()
#   print out who has the money
# 
# #
# def round()
#   first_player = round_setup()
#   print(player name starts)
#   turn(first_player)
#
#   while word != guessed
#       if player_num = 2
#           turn(0)
#       else
#           turn(player_num+1)
#   cash_out()
#   print "round is over, this is how much money you have
#       print_score()
#   
#
# def final_round()
#   player_num = player with max value in the bank
#   get_word()
#   guess_letter for r, s, t, l, n, e
#   print("you get to guess three more consonants and one more vowel")
#   while guessed != word
#       consonant = 0
#       while consonant < 3
#           letter = input("guess a consonant")
#           guess_letter(letter, player_num)
#           consonant = consonant + 1
#       letter = input("guess a vowel: ")
#       guess_letter(letter, player_num)
#       break
#   if guessed != word
#       sorry, you lost
#   else 
#       congratulations, you won an extra $1000!
#       add to roundbank
#       cash_out()
#       display final score
#
#
#
#


# ######################
# game
#   player_setup()
#   for i in range(0,3)
#       if i in [0,1]
#           round()
#       else
#           final_round()
#   print("thanks for playing")
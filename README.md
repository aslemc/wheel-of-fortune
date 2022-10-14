# wheel-of-fortune

This repository contains my first Python assessment for my Dev10 training, in which I created a simple Wheel of Fortune-type game.

I was provided with the following requirements:
* Allow exactly three players
* All three players play the first & second rounds, which end when the word is guessed
* The player with the highest bank plays the third round
* The game ends after round 3
* Gameplay follows this structure:
** The player spins the wheel
** The turn ends when the player lands on "lose a turn" or "bankrupt" (which also empties the round bank) or when they make an incorrect guess
** If the wheel lands on a dollar amount, they can guess a consonant
** The player can buy a vowel if they have enough money
* The final round proceeds as follows:
** Begin with R, S, T, L, N, E revealed
** The player can pick three more consonants and one more vowel
** If they guess the final answer, display their cash prize
* The wheel includes 19 segments which include at least one lose a turn segment, at least one bankrupt segment, and several cash prize segments with varying amounts


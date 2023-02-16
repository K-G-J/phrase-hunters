from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ['my cup of tea', 'a little bird told me',
                        'happy as a clam', 'down to earth', 'a dime a dozen']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = Phrase(self.get_random_phrase())
        self.active_phrase.display()
        game_active = True
        while game_active:
            guess = self.get_guess()
            if self.active_phrase.check_letter(guess):
                print("\nYay! ⭐️ You guessed a letter right!\n")
                if self.active_phrase.check_complete():
                    self.game_over('win')
                    game_active = False
            else:
                self.missed += 1
                print(
                    f"\nSorry 😕 {guess} is not in the phrase\nYou have {5 - self.missed} lives remaining\n")
                if self.missed == 5:
                    self.game_over('loss')
                    game_active = False

    def welcome(self):
        name = input("\nWhat is your name?  ")
        return print(f"\nWelcome {name} to the Phrase Hunters game! 😄\n")

    def get_random_phrase(self):
        return self.phrases[random.randint(0, len(self.phrases) - 1)]

    def get_guess(self):
        while True:
            guess = input("Please guess a letter:  ")
            if not guess.isalpha():
                print("Oops 😕 ... that is not a letter")
                continue
            if len(guess) > 1:
                print("Oops 😕 ... only guess one letter")
                continue
            elif guess in self.guesses:
                print('You already guessed that letter!')
                continue
            else:
                self.guesses.append(guess)
                self.active_phrase.guessed_letters.append(guess)
                self.active_phrase.display()
            return guess

    def game_over(self, outcome):
        if outcome == 'win':
            return print(f'\nYou win! 🌟\n{self.active_phrase}\nCongrats you guessed the phrase! 🥳\n')
        else:
            return print('\nSorry you lost 😕\nbetter luck next time!\n')


if __name__ == '__main__':
    game = Game()
    game.start()

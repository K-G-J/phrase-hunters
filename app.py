from phrasehunter.game import Game

if __name__ == '__main__':
    while True:
        game = Game()
        game.start()
        while (replay := (input("Would you like to play again? (y/n)  ")).lower()) != "n":
            if replay == "y":
                break
            else:
                print('\nPlease enter either "y" or "n"')
        else:
            print("\nThank you for playing Phrase Hunters 👋\n")
            break

"""
Create the Game class in the game.py file
The class should include an initializer or def __init__ method that sets the following attributes:

    missed: used to track the number of incorrect guesses by the user. The initial value is 0 since no guesses have been made at the start of the game.
    phrases: a list of five Phrase objects to use with the game. A phrase should only include letters and spaces -- no numbers, punctuation, or other special characters.
    active_phrase: This is the Phrase object that's currently in play. The initial value will be None. Within the start() method, this property will be set to the Phrase object returned from a call to the get_random_phrase() method.
    guesses: This is a list that contains the letters guessed by the user.

The class should also have these methods:

    start(): Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
        - For each run of the game, a random phrase should be selected from a list of phrases (no punctuation or numbers in phrases, and a phrase must be comprised of more than one word).
        - Before a player has made their first guess, the active phrase should be displayed to the player with underscores as placeholders for the letters. Any spaces between words in the phrase must be clearly visible to the player.

    get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.

    welcome(): this method prints a friendly welcome message to the user at the start of the game

    get_guess(): this method gets the guess from a user and records it in the guesses attribute
        - The game must prompt the player's guess on every turn.
        - After every guess, the game should check whether or not the guessed letter is in the active phrase:
            - After every correct guess, the underscored phrase should be displayed again with any correctly guessed letters in place of the associated underscore.
            - After every incorrect guess, the number missed should increase by one. The game is over when the user has guessed incorrectly five times.

    game_over(): this method displays a friendly win or loss message and ends the game.
        - When the game is over, due to either win or loss, a message must be displayed to the user, and the game must not prompt for another guess.

The Game instance might be responsible for things like starting the game loop, getting the player's input() guesses to pass to a Phrase object to perform its responsibilities against, determining if a win/loss happens after the player runs out of turns or the phrase is completely guessed.
"""

"""
Assignment:     08 Prove: Assignment Milestone
    author:     Freeman Moyo
    Date created: 01 November 2022
    Date modified: 
"""

# import random module
import random

guess_word = ["sausage", "blubber", "pencil", "cloud", "moon", "water", "computer", "school", "network", "hammer", "walking", "violently", "mediocre", "literature", "chair", "two", "window", "cords", "musical", "zebra", "xylophone", "penguin", "home", "dog", "final", "ink", "teacher", "fun", "website", "banana", "uncle", "softly", "mega", "ten", "awesome", "attatch", "blue", "internet", "bottle", "tight", "zone", "tomato", "prison", "hydro", "cleaning", "telivision", "send", "frog", "cup", "book", "zooming", "falling", "evily", "gamer", "lid", "juice", "moniter", "captain", "bonding", "loudly", "thudding", "guitar", "shaving", "hair", "soccer", "water", "racket", "table", "late", "media", "desktop", "flipper", "club", "flying", "smooth", "monster", "purple", "guardian", "bold", "hyperlink", "presentation", "world", "national", "comment", "element", "magic", "lion", "sand", "crust", "toast", "jam", "hunter", "forest", "foraging", "silently", "tawesomated", "joshing", "pong"]
#print(random.choice(guess_word))
guess_word = random.choice(guess_word)
guess_word = guess_word.lower()
#print(guess_word)
display="_"*len(guess_word)
tries=20

#game_over refers to the conditions to be met
#for the game to be over
#it can be, exceeding the needed tries or winning the game
game_over = False
print('Welcome to our game of guessing a random word')
#key word 'not'
while not game_over:
    print('Your guess word is '+ str(len(guess_word)) + ' characters long')
    print('You have '+ str(tries) + ' remaining')
    print("Word", display)
    guess = input('Please input a letter\n: ')
    guess = guess.lower()
    
    #we are now using indexing, to 
	#find the position of the letter in our word
	#we initialise the value of to 0
	#so that we start looking from the beginning
    i = 0
    if guess in guess_word:
        #its (guess, i) not (guess), because (guess) = (guess, 0)
		#if it is 0, it will start searching at the 0 position, which
		#is not ok, we want to search from where we found the character
		#in question. we will continue finding until -1, when we cant find 
		#the guess word anymore
        while guess_word.find(guess, i) != -1:
            i = guess_word.find(guess, i)
            #we are replacing the ith element with the guess letter
			#we check upto before the ith element and after the ith element
            display = display[:i] + guess + display[i + 1:]
            #then increament the i
            i += 1
        for letter in guess_word:
            if letter in guess:
                print(letter, end=" ")
            else:
                print('_', end=" ")
        print('')
        #print('Correct')
        #in the event your guess is not part of the word
    else:
        print('Sorry, wrong guess')
        tries -= 1
    if display == guess_word:
        print('That is correct, the word is ' + guess_word.upper() +'!!!!!!!!!!!!!!!')
        game_over = True
    if tries == 0:
        print('Sorry, you have exhausted all your chances, game over')
        print('The word is ' + guess_word.upper())
        game_over = True
	

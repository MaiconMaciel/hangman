word_list = ["hangman", "python", "code", "game", "computer", "programming", "challenge", "fun", "learning", "guess",
             "banana", "apple", "orange", "grape", "strawberry", "watermelon", "kiwi", "blueberry", "pineapple", "pear",
             "cat", "dog", "bird", "fish", "rabbit", "hamster", "turtle", "horse", "snake", "frog",
             "house", "car", "bicycle", "train", "plane", "boat", "motorcycle", "truck", "bus", "helicopter",
             "book", "pen", "pencil", "paper", "notebook", "marker", "eraser", "crayon", "scissors", "glue",
             "school", "teacher", "student", "classroom", "desk", "chalkboard", "homework", "test", "grade", "lesson",
             "music", "guitar", "piano", "drums", "violin", "trumpet", "flute", "saxophone", "keyboard", "bass",
             "movie", "actor", "actress", "director", "cinema", "popcorn", "ticket", "screen", "camera", "film",
             "pizza", "burger", "fries", "sandwich", "salad", "soup", "pasta", "steak", "sushi", "taco",
             "beach", "mountain", "park", "forest", "lake", "river", "ocean", "island", "desert", "canyon"]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import random



def hangman():
    print('Welcome to the hangman.py')
    lives = 6 #vidas
    print(f'Your live: {lives}')
    x = random.randint(0, len(word_list) - 1) #random para escolher a palavra
    word_to_guess = word_list[x] #palavra a ser advinhada


    # criar uma visualização da palavra, _ de todas as letras
    vis = []
    for x in word_to_guess:
        vis.append('_')
    vis_str = ''.join(vis)
    print(f'Word to guess: {vis_str}')
    #print(vis_str)
    #print(word_to_guess)

    #keep track da letras tentadas
    tried = []
    while lives != 0 and vis_str != word_to_guess:
        tried_letter = input('Input a letter: ')



        if tried_letter in alphabet:
            tried.append(tried_letter)
            tried_str = ''.join(tried)
            print(f'letters tried so far: {tried_str}')

            if tried_letter in word_to_guess:
                for index, letter in enumerate(word_to_guess):
                    if tried_letter == letter:
                        vis[index] = tried_letter
                        vis_str = ''.join(vis)
                        print(f'Word to guess: {vis_str}')
                        if vis_str == word_to_guess:
                            print(f'You have guessed the word "{word_to_guess}", congrats!')
                            print(f'With {lives} lives left')
                            break
            elif tried_letter not in word_to_guess:
                lives -= 1
                print(f'Wrong letter, lives remaining: {lives}')
                print(f'Word to guess: {vis_str}')

            elif tried_letter not in alphabet:
                print('Invalid, try again')
                break

    if lives == 0:
        print(f'You\'ve ran out of lives, you ded now \n The word was "{word_to_guess}"')


    #mostrar a palvra com as letras acertadas e underline no resto
    #quando a letra tiver no vis[] colocar o num













hangman()


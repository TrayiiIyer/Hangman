import turtle
import random
hMan = turtle.Pen()
mark = hMan.clone()
msg = hMan.clone()

def messenger(text):
    '''
    This function writes a message for the player
    Input: the text to write
    Output: none
    '''
    msg.undo()
    msg.write(text,move = False, font = ('Times New Roman', 20, 'normal'))
    return

def intialiseGame():
    '''
    This function sets the board for a game of Hangman.
    Input: none
    Output: none
    '''
    messenger('This is a game of hangman.')
    #Setting the position for the HangPole
    hMan.reset()
    hMan.up()
    hMan.setpos(-300,-100)
    hMan.down()
    #Making the HangPole
    hMan.forward(50)
    hMan.right(180)
    hMan.forward(25)
    hMan.right(90)
    hMan.forward(200)
    hMan.right(90)
    hMan.forward(50)
    hMan.right(90)
    hMan.forward(25)
    hMan.right(90)
    print(hMan.pos())


def generate_words():
    '''
    This function generates a list of candidate words.
    Input:none
    Output: returns a word list: e.g. ['Apple','Blue','Copper','Domain','Elephant']
    '''
    wrdLst = ['four','five','words','temporary','caramel']
    return wrdLst

def wrdPick(lst):
    '''
    This function picks a random word from a list of words.
    Input: a word list: e.g. ['Apple','Blue','Copper','Domain','Elephant']
    Output: a single word, as a string
    '''
    indx = random.randint(0,len(lst)-1)
    return lst[indx]

def line_maker(x,y):
    '''
    This function makes one line at a given coordinate.
    Input: coorinates for a starting point
    Output: the position your turtle is at
    '''
    #Going into position
    mark.up()
    mark.setpos(x,y)
    #Making the dash
    mark.down()
    mark.setpos(x + 20, y)
    return mark.pos()

def make_blanks(wrd):
    '''
    This function makes the lines to write each letter on.
    Input: a word
    Output: none
    '''
    cnt = 0
    x = -300
    y = -300
    while cnt < len(wrd):
        x,y = line_maker(x,y)
        x = x + 10
        cnt = cnt + 1
    messenger("Pick a letter!")
    return

def check_letter(word, letter):
    '''
    This function checks if your guess is correct.
    Input: the challenge word, the guessed letter
    Output: the results (a vector representation showing 1's and 0's where the guessed letter appears respectively)
    '''
    #Declare the results of a list
    results = []
    cnt = 0
    #Checking each character of the given word with the given letter
    while len(results) < len(word):
        if word[cnt].lower() == letter.lower():
            results.append(1)
        else:
            results.append(0)
        #If we find the letter, we add a 1 into the list results. Else we add a zero
        cnt = cnt +1
    return results

def guess_letter(challenge):
    '''
    This is the main function that executes the game.
    Input: the challenge word
    Output: none
    '''
    #Declaring two variables to store the coordinates of a starting position (which we'll need to go back to later, to make the arms and legs)
    neckX, neckY = -225,55
    thighX, thighY = -225,15
    #Declaring a variable to keep track of when to end the game
    isGameOn = True
    #Declaring a variable to keep count of all the wrong guesses
    wrongGuesses = 0
    #Declaring a variable to keep count of all the rightly-guessed letters
    rightGuesses = 0

    #Declaring a dictionary to store the mistake number as a Key, and the body part to draw as a Value
    hangMan_Dict = {1:'head', 2:'body', 3:'rArm', 4:'lArm', 5:'rLeg', 6:'lLeg'}
    
    #Taking inputs from the player
    while isGameOn:
        letter = input('Guess the letter: ')
        result = check_letter(challenge,letter)
        print(result)
        
        if result.count(1) == 0:
            wrongGuesses = wrongGuesses +1
            #Making the next part of the poor man hanging
            make_hangMan(hangMan_Dict[wrongGuesses],neckX,neckY,thighX,thighY)
            messenger('Oops... better luck next time!')
        
        else:
            rightGuesses = rightGuesses + result.count(1) #we have to change this logic to avoid double counting the correct letters
        #Since the guess was correct, write the letter in it's respective dash
            make_letters(letter,result,genCoordinates(challenge,-300,-300))
            messenger('Yes! Keep going!')
       
        if wrongGuesses >5:
            isGameOn = False
            print("Game over!")
            messenger('Game over!')
        
        elif rightGuesses == len(challenge):
            isGameOn = False
            print("You win!")
            messenger('You win!')
    return

def make_hangMan(part,neckX,neckY,thighX,thighY):
    '''
    This function makes a part of the hangman.
    Input: which part to make (head, body, arms, or legs)
    Output: none (might have one, though)
    '''
    #Writing a function to make all the different parts of the body.
    hMan.up()
    #Making the head
    if part == 'head':
        hMan.down()
        hMan.circle(10)
    #Making the body
    elif part == 'body':
        hMan.setpos(neckX,neckY)
        hMan.down()
        hMan.setpos(neckX,neckY - 40)
    #Making the right arm
    elif part == 'rArm':
        hMan.setpos(neckX,neckY)
        hMan.down()
        hMan.setpos(neckX - 10, neckY - 20)
    #Making the left arm
    elif part == 'lArm':
        hMan.setpos(neckX,neckY)
        hMan.down()
        hMan.setpos(neckX + 10, neckY - 20)
    #Making the right leg
    elif part == 'rLeg':
        hMan.setpos(thighX, thighY)
        hMan.down()
        hMan.setpos(thighX - 10, thighY - 20)
    #Making the left leg
    elif part == 'lLeg':
        hMan.setpos(thighX, thighY)
        hMan.down()
        hMan.setpos(thighX + 10, thighY - 20)
    hMan.up()

def genCoordinates(challenge,x,y):
    '''
    This function builds a dictionary of coordinates, for every letter in the Challenge Word.
    Input: the challenge word, and the coordinates for the starting position
    Output: it returns the new coordinates, depending on how long the word was
    '''
    cnt = 0
    coordinates = {}
    while cnt < len(challenge):
        x_y_Lst = [x,y]
        coordinates[cnt] = x_y_Lst
        x = x +30
        cnt = cnt +1
    return coordinates

def make_letters(letter,result,coorDict):
    '''
    This function makes the guessed letter (if you guessed correctly)
    Input: the letter to be drawn, result (a vector representation showing 1's and 0's where the guessed letter appears respectively), coorDict (a coordinate dictionary)
    Output: none
    '''
    cnt = 0
    while cnt < len(result):
        if result[cnt] == 1:
            x,y = coorDict[cnt]
            mark.up()
            mark.setpos(x,y)
            mark.write(letter,move = False, font = ('Times New Roman', 20, 'normal'))
        cnt = cnt +1
    return

intialiseGame()

Lst = generate_words()
challenge = wrdPick(Lst)

make_blanks(challenge)
guess_letter(challenge)
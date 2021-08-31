import random
from termcolor import cprint, colored

# list of word possible for guess
words = ["dog","rome","cambridge","table"]

#dictionary to draw hangman with key(s); 0,1,2,3,4,5,6,7
draw_man = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |        / | \\
               |          |
               |        /   \\
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |        / | \\
               |          |
               |        /   
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |        / | \\
               |          |
               |           
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |        / | 
               |          |
               |           
            """,
        4: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          | 
               |          |
               |           
            """,
        5: """
                ___________
               | /        | 
               |/        ( )
               |
               |
               |
               |
            """,
        6: """
                ___________
               | /        | 
               |/
               |
               |
               |
               |
            """,

        7: "",
    }

#function to guess random word from the list of word available 
def pick_word(words):
  word = random.choice(words)

  while "_" in word: # letters in word to be rep as "_" untill its guessed
    word = random.choice(words)
  return word.lower() #  word to be in lower case

word = pick_word(words) #word

#function to give hint
def give_hint():
  if word == "dog":
    hint = "animal"
  if word == "rome":
    hint = "place"
  if word == "cambridge":
    hint = "school"
  if word == "table":
    hint = "object"
  return hint

Hint = give_hint() #hint

#function hangman
def hangman():
  letters = set(word) #letters in word
  right = set() #right guess(letter) in word
  wrong = set() #wrong guess(letter)
  chances = 7  #live

  while chances > 0 and len(letters) > 0:

    print(colored("HINT:"+ Hint, "white", "on_red"))
    print("wrong guesses:", " ".join(wrong),"\n")
    print("You have",chances,"chances left")

    word_entry = [letter if letter in right else "_" for letter in word] # word_entry display "_" unless right letter is guessed

    print(draw_man[chances]) # space to display hangman

    print("Current word:", " ".join(word_entry)) 

    letter_entry = input("Guess a letter: ").lower() # make a guess, letter will be in lower case

    if letter_entry not in wrong: 

      if letter_entry in word:
        letters.remove(letter_entry) #letter guessed is remove from letters in the word
        right.add(letter_entry)  #right guess is added to right set ()
        print("")

      else:
        chances -=  1  #wrong guess reduces chances  by 1 
        print('\nletter:', letter_entry, ',is not in the word.')
        wrong.add(letter_entry)  #wrong guess is added to wrong set()
    
    elif letter_entry in wrong:
      print('\nYou have already used that letter. Guess another letter.') # error if wrong guess is guessed again

    else:
      print('\nThat is not a valid letter.')

  if chances == 0: 
        print(draw_man[0])
        print('You died, sorry. The word was', word)
  elif len(letters) == 0: # if word is guessed
      print('YAY! You guessed the word', word, '!!')
    
if __name__ == '__main__':
    hangman()

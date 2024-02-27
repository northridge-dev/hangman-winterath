from ascii_art import BANNER, HANGMAN_PICS
import os
from time import sleep
import random




play_again = True


def play_hangman():
  

  small_list = ['analog', 'algorithm','button','banned','chronology','clock','dexterity','duplicate','extension', 'enter','fickle','faulty','gallant','games','halberd','hand','integral','instead','jolly','joke','knock','know','lamb','lock','method','madness','nothing','narcotic','optimized','oral','perfection','plotting','quit','quadruple','runner','ravage','syntax','slither','tangible','tally','under','ulterior','vexing','violet','wane','wacky','xylophone','xenophobia','yonder','yell','zebra','zesty']
  alt_word = random.choice(small_list)



  word = input("Welcome to Hangman!\nChoose a word for your opponent to guess, or press Enter for a random one.\n->")
  if word == '':
    word = alt_word
  wordlist = ([*word])
  sleep(5)
  os.system('clear')
  
  
  hidden_wordlist = []
  for i in range(len(wordlist)):
    hidden_wordlist.append(" _")

  correct = []
  wrong = []
  guessed =[]
  guesses_left = 6

  def display_stats():
    print(HANGMAN_PICS[guesses_left])
    print("".join(hidden_wordlist))
    print(f"You have {guesses_left} guesses left.")
    print(f"Correct guesses: {correct}")
    print(f"Wrong guesses: {wrong}")
    sleep(0.5)








  play_again = False
  stayin_alive = True

  while stayin_alive:
    
    display_stats()
    guess_loop = True
    guess = input("Guess a letter (that you haven't guessed already).\n->")
    if guess == 'quit':
      exit()


      
    
    while guess_loop:

      repromptu_count = 0
      guess_loop = False
      if len(guessed) !=0:
       for o in range(len(guessed)):
          if guess == guessed[repromptu_count]:
            guess = input("\nGuess a letter (that you haven't guessed already).\n->")
            guess_loop = True
          repromptu_count += 1



    wrogi_count = 0
    count = 0 

    for ii in range(len(wordlist)):
      if guess == wordlist[count]:
        print(f"{guess} is correct!")
        correct.append(guess)
        wordcount = 0
        for DOCTOR_KRUCKENBERG in range(len(wordlist)):
          if guess == wordlist[wordcount]:
            hidden_wordlist[wordcount] = f' {guess}'
          wordcount+=1

        if len(correct) == len(wordlist):
          print(f"You guessed the word! the word was {word}.")
          play_gain = input("Enter if you wish to play again. Otherwise type anything and Enter\n->")
          if play_gain != '':
            exit()
          stayin_alive = False
          
          
      
      else:
        wrogi_count += 1
        if wrogi_count == len(wordlist):
          print(f"{guess} is wrong!")
          wrong.append(guess)
          guesses_left -= 1
      

      if guesses_left == 0:
        (f"You couldn't guess the word! The word was {wordlist}.")
        play_again = input("Enter if you wish to play again. Otherwise type anything and Enter\n->")
        if play_again != '':
          exit()
        stayin_alive = False
        
      count+=1
    sleep(1)
    os.system('clear')
    guessed.append(guess)








play_hangman()
while play_again:
  play_hangman()
os.system('clear')
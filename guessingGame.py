import random
name = input("Enter your Name: ")
print(f"Hello {name}! Welcome to the Guessing Game")
words = ["apple", "orange", "guava", "python"]
word = words[random.randint(0, len(words))]
guesses = word[random.randint(0, len(word))] + \
    word[random.randint(0, len(word))]
tries = 10
choice = "Yes"


def playAgain():
    global choice
    choice = input("Do you want to play again? Yes/No :\n")
    if choice == "Yes":
        global word, guesses, tries
        word = words[random.randint(0, len(words))]
        guesses = word[random.randint(
            0, len(word))] + word[random.randint(0, len(word))]
        tries = 10


while choice == "Yes":
    while (tries > 0):
        won = True
        for chr in word:
            if chr in guesses:
                print(chr, end="")
            else:
                print("-", end="")
                won = False
        if (won):
            print(f"\nYou've won the game! Your score is {tries} out of 10")
            playAgain()
            break
        ch = input("\nGuess a character: ")
        if (ch in word):
            guesses += ch
        else:
            print("Wrong answer")
            tries -= 1
            print(f"You have {tries} left")
        if tries == 0:
            print("You lose!")
            playAgain()
            break
print("Thanks for playing!")

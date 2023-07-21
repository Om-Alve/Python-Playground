

def main():
    text = input("Text: ")
    letters = numOfLetters(text)
    words = numOfWords(text)
    sentences = numOfSentences(text)
    grade(letters, words, sentences)

# Count the number of letters in given text


def numOfLetters(text):
    letters = 0
    i = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        i += 1
    return letters

# Count the number of words in given text


def numOfWords(text):
    words = 1
    for i in range(len(text)):
        if (text[i] == ' '):
            words += 1
        i += 1
    return words

# Count the number of sentences in given text


def numOfSentences(text):
    sentences = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            sentences += 1
        i += 1
    return sentences

# Calculate the Coleman-Liau Index


def grade(l, w, s):
    # L -->average number of letters per 100 words and S --> average number of sentences per 100 words
    L = l / (w / 100.0)
    S = s / (w / 100.0)
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index <= 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")
    return


main()

from spacy.pipeline import Sentencizer
from spacy.lang.en import English
import wikipedia
import spacy
from spacy.lang.en import STOP_WORDS

nlp = spacy.load("en_core_web_sm")


# Load the pre-trained NLP model
nlp = spacy.load("en_core_web_sm")
sentencizer = Sentencizer()
nlp.add_pipe('sentencizer', before='parser')


# Define a function to search for a Wikipedia page based on a query and extract its text content


def get_page_content(query):
    # Search for a Wikipedia page based on the query
    search_results = wikipedia.search(query)
    if not search_results:
        return None
    page_title = search_results[0]

    # Retrieve the text content of the page
    text_content = wikipedia.page(page_title).content

    return text_content

# Define a function to find the best answer to a question in a text content


def find_answer(question, text_content):
    # Preprocess the question and text content using spaCy
    question_doc = nlp(question)
    text_doc = nlp(text_content)

    # Find the best answer by comparing the similarity between the question and each sentence in the text content
    best_answer = None
    best_score = 0
    for sent in text_doc.sents:
        score = question_doc.similarity(sent)
        if score > best_score:
            best_answer = sent.text
            best_score = score

    # Return the best answer
    return best_answer


# Define a loop to receive questions from the user and provide answers
while True:
    # Receive a question from the user
    question = input("Ask me a question: ")

    # Search for a Wikipedia page based on the question and extract its text content
    page_content = get_page_content(question)
    if not page_content:
        print("Sorry, I couldn't find a Wikipedia page for your question.")
        continue

    # Find the best answer in the text content and print it
    answer = find_answer(question, page_content)
    print(answer)

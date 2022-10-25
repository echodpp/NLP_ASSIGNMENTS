"""this is a bare-bones Markov text generator"""

from collections import defaultdict
import random

# nltk.download("gutenberg")
# nltk.download('punkt')


def markov_chain(text):
    """The input is a string of text and the output will be a dictionary with each word as
    a key and each value as the list of words that come after the key in the text."""
    # Tokenize the text by word, though including punctuation
    words = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())

    # Initialize a default dictionary to hold all of the words and next words
    corpus = defaultdict(list)

    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        corpus[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    corpus = dict(corpus)
    return corpus


def finish_sentence(sentence, n, corpus, deterministic=True):
    """given a sentence, return the next word
        if deterministic is True, choose at each step the single most probable next
    token
        if deterministic is False, draw the next word randomly from the appropriate distribution.
    Use stupid backoff and no smoothing"""
    # Get the last word
    last_word = sentence[-1]
    # Get the list of next words
    next_words = corpus[last_word]
    # determinisitc = True
    if deterministic:
        # Get the most common word
        most_common = nltk.FreqDist(next_words).max()
        # Return the most common word
        return most_common
    # determinisitc = False
    else:
        # Get the frequency distribution of the next words
        freq = nltk.FreqDist(next_words)
        # Get the probability distribution of the next words
        prob = nltk.MLEProbDist(freq)
        # Get the random word
        random_word = prob.generate()
        # Return the random word
        return random_word
    return None


import nltk

# nltk.download("gutenberg")
# nltk.download('punkt')


print(nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower()))

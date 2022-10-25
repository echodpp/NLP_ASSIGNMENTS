import nltk
import numpy as np

# nltk.download("gutenberg")
# nltk.download('punkt')


def make_dictionary(sentence, corpus, n):
    """
    It takes a sentence, a corpus, and an n-gram length, and returns a dictionary of the n-grams in the
    corpus that follow the sentence

    :param sentence: the sentence we're currently working with
    :param corpus: the text you want to generate a sentence from
    :param n: the number of words in the n-gram
    :return: A dictionary of the next word and the number of times it appears after the sentence.
    """
    dic = {}
    lis = []
    for i in range(0, len(corpus)):
        section = corpus[i : i + (n - 1)]
        if section == sentence[-(n - 1) :]:
            next = corpus[i + (n - 1)]
            lis.append(next)
    for item in lis:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic


def backoff(original, matching, n):
    """
    If the dictionary is empty, decrease n by 1 and try again. If the dictionary is not empty, return
    the key with the highest value.

    :param original: the original word
    :param matching: a list of words that match the original word in terms of length and first and last
    letters
    :param n: the number of words to consider in the context
    :return: the most common word in the dictionary.
    """
    while n > 1:
        dict = make_dictionary(original, matching, n)
        if dict == {}:
            n -= 1
        elif dict != {}:
            return max(dict, key=dict.get)
    return np.random.choice(matching)


def next_word(original, matching, n):
    """
    If the dictionary has only one key, return that key. Otherwise, return the key with the highest
    value

    :param original: the original string
    :param matching: the list of words that match the original word
    :param n: the number of words to look at
    :return: The next word in the sequence.
    """
    dict = make_dictionary(original, matching, n)
    if len(dict) == sum(dict.values()):
        return next(iter(dict))
    else:
        return max(dict, key=dict.get)


def finish_sentence(sentence, n, corpus, deterministic=False):
    """
    It takes a sentence, a corpus, and an n-gram size, and returns a sentence that is finished with a
    period, question mark, or exclamation point

    :param sentence: a list of words
    :param n: the number of words to look at in the corpus
    :param corpus: a list of strings, each string is a sentence
    :param deterministic: if True, the sentence will be finished using the next_word function. If False,
    the sentence will be finished using the backoff function, defaults to False (optional)
    :return: A list of words that make up a sentence.
    """
    while sentence[-1] not in "?!." and len(sentence) < 15:
        if deterministic == True:
            sentence.append(next_word(sentence, corpus, n))
        elif deterministic == False:
            sentence.append(backoff(sentence, corpus, n))
    return sentence

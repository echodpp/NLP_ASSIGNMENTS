# This is a Part-of-speech Tagging example 
Use the first 10k tagged sentences from the Brown corpus to generate the components of a part-of-speech hidden markov model: the transition matrix, observation matrix, and initial state distribution. Use the universal tagset:
nltk.corpus.brown.tagged_sents(tagset=’universal’)[:10000]
Also hang on to the mappings between states/observations and indices. In- clude an OOV/UNK observation and smoothing everywhere.
Using the provided Viterbi implementation, infer the sequence of states for sentences 10150-10152 of the Brown corpus:
nltk.corpus.brown.tagged_sents(tagset=’universal’)[10150:10153]

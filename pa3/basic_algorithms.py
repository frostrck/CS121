"""
CS121: Analyzing Election Tweets (Solutions)

Algorithms for efficiently counting and sorting distinct `entities`,
or unique values, are widely used in data analysis.

Functions to implement:

- count_tokens
- find_top_k
- find_min_count
- find_most_salient

You may add helper functions.
"""

import math
from util import sort_count_pairs

def count_tokens(tokens):
    '''
    Counts each distinct token (entity) in a list of tokens

    Inputs:
        tokens: list of tokens (must be immutable)
    

    Returns: dictionary that maps tokens to counts
    '''
    count = {}
    for val in tokens:
        if val not in count:
            count[val] = 1
        else: 
            count[val] += 1
    
    return count


def find_top_k(tokens, k):
    '''
    Find the k most frequently occuring tokens

    Inputs:
        tokens: list of tokens (must be immutable)
        k: a non-negative integer


    Returns: list of the top k tokens ordered by count.
    '''

    #Error checking (DO NOT MODIFY)
    if k < 0:
        raise ValueError("In find_top_k, k must be a non-negative integer")

    pairs = sort_count_pairs(count_tokens(tokens).items())

    top = []

    if len(pairs) > 0:
        for i in range(min(k, len(pairs))):
            top.append(pairs[i][0])
    
    return top


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur *at least* min_count times

    Inputs:
        tokens: a list of tokens  (must be immutable)
        min_count: a non-negative integer

    Returns: set of tokens
    '''

    #Error checking (DO NOT MODIFY)
    if min_count < 0:
        raise ValueError("min_count must be a non-negative integer")

    min = set()
    count = count_tokens(tokens)
    for key in count:
        if count[key] >= min_count:
            min.add(key)

    return min

def aug_freq(doc):
    '''
    Compute the augmented frequency of a term in a document among a collection of documents.

    Inputs:
        doc: a list of tokens
    
    Returns: dictionary of tokens and their augmented frequencies
    '''
    if doc == []:
        return None
    max = find_top_k(doc, 1)[0]
    count = count_tokens(doc)
    freq = {}
    for token in doc:
        score = 0.5 + 0.5 * (count[token]/count[max])
        freq[token] = score

    return freq

def inv_doc_freq(docs):
    '''
    Computes the inverse document frequency of a token in a collection of documents.

    Inputs:
        docs: a collection of documents aka a list of list of tokens
    
    Returns: dictionary of tokens and their inverse document frequency
    '''
    inv_freq = {}
    N = len(docs)

    count_freq = {}
    for doc1 in docs:
        for token in doc1:
            counter = 0
            for doc2 in docs:
                if token in doc2:
                    counter += 1
            count_freq[token] = counter
            inv_freq[token] = math.log(N / count_freq[token])
    return inv_freq


def find_salient(docs, threshold):
    '''
    Compute the salient words for each document.  A word is salient if
    its tf-idf score is strictly above a given threshold.

    Inputs:
      docs: list of list of tokens
      threshold: float

    Returns: list of sets of salient words
    '''

    salient_tokens = []
    idf = inv_doc_freq(docs)
    for doc in docs:
        tf = aug_freq(doc)
        doc_salient = set()
        for token in doc:
            tf_idf = idf[token] * tf[token]
            if tf_idf > threshold:
                doc_salient.add(token)
        salient_tokens.append(doc_salient)
    
    return salient_tokens

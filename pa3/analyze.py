"""
Analyze module
"""

import unicodedata
import sys

from basic_algorithms import find_top_k, find_min_count, find_salient

##################### DO NOT MODIFY THIS CODE #####################

def keep_chr(ch):
    '''
    Find all characters that are classifed as punctuation in Unicode
    (except #, @, &) and combine them into a single string.
    '''
    return unicodedata.category(ch).startswith('P') and \
        (ch not in ("#", "@", "&"))

PUNCTUATION = " ".join([chr(i) for i in range(sys.maxunicode)
                        if keep_chr(chr(i))])

# When processing tweets, ignore these words
STOP_WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
              "and", "on", "to", "be", "if", "we", "you", "in", "is",
              "at", "it", "rt", "mt", "with"]

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")


#####################  MODIFY THIS CODE #####################


############## Part 2 ##############

# Task 2.1

def generate_tokens(tweets, entity_desc):
    '''
    Given a list of tweets and entity_desc, generate a list of entities
    that appear in those tweets according to entity_desc.

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
    
    Returns: list of entities with duplicates
    '''
    key, subkey, case = entity_desc
    list_tokens = []

    for tweet in tweets:
        entities = tweet["entities"][key]
        for val in entities:
            if case is True:
                list_tokens.append(val[subkey])
            else:
                list_tokens.append(val[subkey].lower())
    
    return list_tokens

def find_top_k_entities(tweets, entity_desc, k):
    '''
    Find the k most frequently occuring entitites

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
        k: integer

    Returns: list of entities
    '''

    list_entities = generate_tokens(tweets, entity_desc)
    
    top_k_entities = find_top_k(list_entities, k)

    return top_k_entities


# Task 2.2
def find_min_count_entities(tweets, entity_desc, min_count):
    '''
    Find the entitites that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
        min_count: integer

    Returns: set of entities
    '''

    list_entities = generate_tokens(tweets, entity_desc)

    least = find_min_count(list_entities, min_count)
    
    return least




############## Part 3 ##############

def preprocess(tweet, case, stop_words = True):
    '''
    Takes in a tweet and convert it into a list of strings.

    Inputs:
        tweet: (dict) a single tweet
        case(bool): whether or not we want to result to be case-sensitive
        stop_words(bool): whether or not we want to include STOP_WORDS

    Returns: list of strings
    '''
    words = tweet['abridged_text'].split()

    prepro = []

    for i, word in enumerate(words):
        words[i] = word.strip(PUNCTUATION)

    if case is False:
        for i, word in enumerate(words):
            words[i] = word.lower()
    
    for word in words:
        if len(word) > 0 and word.startswith(STOP_PREFIXES) is False:
            if stop_words is True:
                if word not in STOP_WORDS:
                    prepro.append(word)
            else:
                prepro.append(word)

    return prepro



def convert_ngrams(tweet, n, case, stop = True):
    '''
    Preprocess a tweet and convert to n-grams

    Input: 
        tweet: a tweet
        n: integer
        case: boolean
        stop: boolean, whether or not to include stop words
    
    Returns: list of n-tuples
    '''

    convert = preprocess(tweet, case, stop)
    ngrams = [convert[i : i + n] for i in range(len(convert) - n + 1)]

    for i, gram in enumerate(ngrams):
        ngrams[i] = tuple(gram)

    return ngrams

def find_top_k_ngrams(tweets, n, case_sensitive, k):
    '''
    Find k most frequently occurring n-grams

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        k: integer

    Returns: list of n-grams
    '''

    all_ngrams = []
    for tweet in tweets:
        convert = convert_ngrams(tweet, n, case_sensitive)
        for gram in convert:
            all_ngrams.append(gram)

    top_k_ngrams = find_top_k(all_ngrams, k)
    
    return top_k_ngrams



def find_min_count_ngrams(tweets, n, case_sensitive, min_count):
    '''
    Find n-grams that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        min_count: integer

    Returns: set of n-grams
    '''

    all_ngrams = []
    for tweet in tweets:
        convert = convert_ngrams(tweet, n, case_sensitive)
        for gram in convert:
            all_ngrams.append(gram)

    min_ngrams = find_min_count(all_ngrams, min_count)

    return min_ngrams

def find_salient_ngrams(tweets, n, case_sensitive, threshold):
    '''
    Find the salient n-grams for each tweet.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        threshold: float

    Returns: list of sets of strings
    '''

    all_tweets = []
    for tweet in tweets:
        all_ngrams = []
        convert = convert_ngrams(tweet, n, case_sensitive, False)
        for gram in convert:
            all_ngrams.append(gram)
        all_tweets.append(all_ngrams)
    
    salient_ngrams = find_salient(all_tweets, threshold)
    
    return salient_ngrams

import colorsys
import datetime
from random import random
import jsonpickle
import re

from numpy.core.numeric import full
from deep_translator import GoogleTranslator
from textblob import TextBlob

import nltk
nltk.download('stopwords')
nltk.download("punkt")

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from faker import Faker

fake = Faker()


# fake.date_between(start_date='today', end_date='+30d')
# fake.date_time_between(start_date='-30d', end_date='now')
#
# # Or if you need a more specific date boundaries, provide the start
# # and end dates explicitly.
# start_date = datetime.date(year=2015, month=1, day=1)
# fake.date_between(start_date=start_date, end_date='+30y')

def get_random_date():
    """Generate a random datetime between `start` and `end`"""
    return fake.date_time_between(start_date='-30d', end_date='now')


def get_random_date_in(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())), )


class Document:
    def __init__(self, id, full_text, created_at, hashtags, user_name, retweet_count, favourites_count, url, user_screen_name):
        self.id = id
        self.full_text = full_text
        self.created_at = created_at
        self.hashtags = hashtags
        self.user_name = user_name
        self.retweet_count = retweet_count
        self.favourites_count = favourites_count
        self.url = url
        self.user_screen_name = user_screen_name


def load_documents_corpus():
    """
    Load documents corpus from dataset_tweets_WHO.txt file
    :return:
    """

    ##### demo replace ith your code here #####
    corpus_terms = []
    path = 'data/'
    docs_path = path + 'dataset_tweets_WHO.txt'

    with open(docs_path) as f:
        for line in f:
            docs = jsonpickle.decode(line)
            full_txts = get_full_text(docs)
            for id_str in full_txts:
                corpus_terms.append({
                    'tweet_id' : id_str,
                    'terms' : extract_terms(full_txts[id_str])
                })

    tweets = format_documents(docs)
    return tweets,corpus_terms


def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

def get_full_text(docs):

    # Put tweets (only full_text) in a list in order to apply Data Processing
    full_txts = {}
    for i in range(len(docs)):
        text = docs[str(i)]['full_text']
        if docs[str(i)]['lang'] != 'en':
            text = translate(text)
        full_txts[docs[str(i)]['id_str']] = text
    return full_txts


def extract_terms(line):
    """

    """

    stemmer = PorterStemmer()
    stop_words = set(stopwords.words("english"))

    line = re.sub(r"http\S+", "", line)  # Remove URL
    line = line.lower()  # Transform in lowercase
    words = nltk.word_tokenize(line)  # Split tweets into words
    line = line.split()
    # Tokenize the text to get a list of terms and remove puntuation
    line = [word for word in words if word.isalnum()]
    line = [word for word in line if word not in stop_words]  # Remove Stopwords
    line = [word for word in line if word.isascii()]  # Remove Stopwords
    line = [stemmer.stem(word) for word in line]  # Perform stemming

    return line
def format_documents(docs):
    tweets = []
    for doc in docs.values():
        url = 'https://twitter.com/' + doc['user']['screen_name'] + '/status/' + doc['id_str'] + ' '
        hashtags = [hashtag['text'] for hashtag in doc['entities']['hashtags']]
        full_text = doc['full_text']
        if doc['lang'] != 'en':
            full_text = translate(full_text)
        tweet = Document(
            doc['id_str'],
            full_text,
            doc['created_at'],
            hashtags,
            doc['user']['name'],
            doc['retweet_count'],
            doc['favorite_count'],
            url,
            doc['user']['screen_name'],
        )
        tweets.append(tweet)
    return tweets

def parse_results(tweets,idxs):
    document_results = []
    for index in idxs:
        document_results.append(tweets[index])
    return document_results

def get_palette(N):
    HSV_tuples = [(x*255.0/N, x*156/N, x*73/N) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    print(RGB_tuples)
    return list(RGB_tuples)

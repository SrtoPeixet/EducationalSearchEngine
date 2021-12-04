import random
from app.core import utils
from app.search_engine import algorithms

from app.core.utils import get_random_date

class SearchEngine:
    """educational search engine"""
    i = 12345
    tweet2vec = []

    def set_corpus(self,corpus_terms):
        terms = []
        for pair_term in corpus_terms:
            terms.append(pair_term['terms'])
        self.tweet2vec = algorithms.tweet_2_vec(terms)

    def search(self, search_query):
        print("Search query:", search_query)
        query_terms = utils.extract_terms(search_query)
        query2vec = algorithms.tweet_2_vec(query_terms)[0] #We only have 1 query, acess to the position!
        results_index = algorithms.cosine_similarity(self.tweet2vec,query2vec)
        return results_index
    


class DocumentInfo:
    def __init__(self, title, description, doc_date, url, ranking):
        self.title = title
        self.description = description
        self.doc_date = doc_date
        self.url = url
        self.ranking = ranking

from utils import *

class Vectorial:
    def __init__(self, dataset: list, k: int = 10):
        self._vocabulary = get_vocabulary(dataset)
        self._vectors = get_word_counts(dataset, self._vocabulary)
        self._k = k

    def make_query(self, query: str):
        query_vector = get_word_counts(parse_query(query), self._vocabulary)
        cosine_similarity = get_cosine_similarity(query_vector, self._vectors)
        answer = sorted(cosine_similarity, key=cosine_similarity.get, reverse=True)[:self._k]
        return answer
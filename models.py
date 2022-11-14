from utils import *

def vectorial_model(query:str, dataset:list, k:int = 10):
    # query: string
    # k: number of documents to return
    # return: list of k documents (ids) sorted by relevance
    raw_documents = dataset.append(query)
    vocabulary = get_vocabulary(raw_documents)
    vectors = get_word_counts(parse_documents(dataset), vocabulary)
    query_vector = get_word_counts([parse_document(query)], vocabulary)
    cosine_similarity = get_cosine_similarity(query_vector, vectors)
    answer = sorted(cosine_similarity, key=cosine_similarity.get, reverse=True)[:k]
    return answer
    
    
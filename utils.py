import numpy as np
import pandas as pd
from re import compile, match

def parse_query(query):
    """Parse query into a list of words."""
    pattern = compile(r'[\w\W]*[ ]+[\w\W]*')
    if match(pattern, query):
        return query.split()
    return [query]

def parse_document(document):
    """Parse document into a list of words."""
    parsed_document = []
    pattern = compile(r'\w*[\d\.\,]+\w*')
    lines = document.split('\n')
    for line in lines:
        for word in line.split():
            if match(pattern, word):
                continue
            parsed_document.append(word)
    return parsed_document[1:]
       

def parse_documents(documents):
    """Parse documents into a list of words by document."""
    return [parse_document(document) for document in documents]
    
def get_vocabulary(documents):
    """Get vocabulary from documents."""
    vocabulary = []
    for document in documents:
        for word in document:
            if not word in vocabulary:
                vocabulary.append(word)
    return vocabulary

def get_word_counts(documents, vocabulary):
    """Get word counts from documents."""
    word_counts = pd.DataFrame(0, index=np.arange(len(documents)), columns=vocabulary)
    for i, document in enumerate(documents):
        for word in document:
            word_counts[word][i] += 1
    return word_counts
    
def get_cosine_similarity(query, vectors):
    """Get cosine similarity from vectors."""
    dot_products = vectors.dot(vectors.T)
    norms = np.linalg.norm(vectors, axis=1)
    query_norm = np.linalg.norm(query)
    cosine_similarity = {}
    for i, norm in enumerate(norms):
        cosine_similarity[i] = dot_products[i][i] / (norm * query_norm)
    return cosine_similarity

def get_word_frequencies(documents):
    """Get word frequencies from documents."""
    word_counts = get_word_counts(documents)
    word_frequencies = word_counts / word_counts.sum(axis=1)[:, np.newaxis]
    return word_frequencies

def get_word_probabilities(documents):
    """Get word probabilities from documents."""
    word_counts = get_word_counts(documents)
    word_probabilities = word_counts / word_counts.sum(axis=0)
    return word_probabilities
    
def get_word_log_probabilities(documents):
    """Get word log probabilities from documents."""
    word_probabilities = get_word_probabilities(documents)
    word_log_probabilities = np.log(word_probabilities)
    return word_log_probabilities

def get_word_log_probabilities_smoothed(documents, alpha=1):
    """Get word log probabilities from documents."""
    word_counts = get_word_counts(documents)
    word_log_probabilities = np.log((word_counts + alpha) / (word_counts + alpha).sum(axis=0))
    return word_log_probabilities

def get_word_log_probabilities_smoothed_with_pseudocounts(documents, alpha=1):
    """Get word log probabilities from documents."""
    word_counts = get_word_counts(documents)
    word_log_probabilities = np.log((word_counts + alpha) / (word_counts + alpha).sum(axis=0))
    return word_log_probabilities
    
def get_word_idf(documents):
    """Get word idf from documents."""
    word_counts = get_word_counts(documents)
    word_idf = np.log(len(documents) / word_counts.astype(bool).sum(axis=0))
    return word_idf

def get_word_tf_idf(documents):
    """Get word tf-idf from documents."""
    word_frequencies = get_word_frequencies(documents)
    word_idf = get_word_idf(documents)
    word_tf_idf = word_frequencies * word_idf
    return word_tf_idf
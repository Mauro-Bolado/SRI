import os
import sys
from models import *


def parse_dataset(dataset_path):
    # Read the dataset
    with open(dataset_path, 'r') as f:
        dataset = f.read()[2:].split('\n.I ')
        data = parse_documents(dataset)
    return data

def main():
    # Read the query in the argument 1
    query = sys.argv[1]
    # Read the dataset in the argument 2
    data = sys.argv[2]
    
    raw_documents = parse_dataset(data)
    dataset = raw_documents.__add__(parse_query(query))
    print(vectorial_model(query, dataset))
    
    
    
if __name__ == '__main__':
    main()
    

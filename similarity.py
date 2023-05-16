import ast
import pandas as pd
import numpy as np

from text_embedding import get_embedding

def vector_similarity(vec1, vec2):
    return np.dot(np.array(vec1), np.array(vec2))


if __name__ == '__main__':
    prompt = input('Prompt: ')
    prompt_embedding = get_embedding(prompt)
    df = pd.read_csv('jira_with_vector.csv')
    df['similarity'] = df['embedding'].apply(
        lambda vector: vector_similarity(ast.literal_eval(vector), prompt_embedding)
    )
    print(df.nlargest(10, 'similarity'))

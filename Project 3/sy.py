'''Semantic Similarity

Authors: Danial Hasan, Dylan Vogel, and Michael Guerzhoy. Last modified: Nov. 29, 2016.
'''

import math


def norm(vec):
    ''' Return a float of the norm of a vector vec stored as a dictionary.
        Assume all dictionary values are ints'''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    ''' Return a float of the cosine similarity of two vectors vec1, vec2, stored as        
        dictionaries. 
        Assume all dictionary values are ints, and that neither vector is empty.'''
        
    dot_prod = 0
    for a in vec1:
        if a in vec2:
            dot_prod += vec1[a] * vec2[a]
    magnitude_prod = norm(vec1) * norm(vec2)
        
    return dot_prod/magnitude_prod
    
def euclidian_similarity(vec1, vec2):
    ''' Return a float of the negative distance in Euclidian space between two vectors 
        vec1, vec2, stored as dictionaries.
        Assume all dictionary values are ints'''
    
    combined_vec = {**vec1, **vec2}
    vector_sub = {}
    
    for word in combined_vec:
        vector_sub[word] = vec1.get(word, 0) - vec2.get(word, 0)
    
    return norm(vector_sub) * -1

def euclidian_similarity_norm(vec1, vec2):
    ''' Return a float of the negative distance in Euclidian space between two normalized 
        vectors vec1, vec2, stored as dictionaries.
        Assume all dictionary values are ints, and that neithe vector is empty'''
    
    vector_sub = {}
    
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    
    combined_vec = {**vec1, **vec2}
    
    for word in combined_vec:
        vector_sub[word] = (vec1.get(word, 0) / norm1) - (vec2.get(word, 0) / norm2)
        
    return norm(vector_sub) * -1
            

def build_semantic_descriptors(sentences):
    ''' Return a dictionary whose values are a dictionary of the number of times a word
        appears alongside the key word across all sentences in sentences.
        Assume sentences is a list of a list of strings '''
        
    d = {}
    for sentence in sentences:
        words_in_sent = []
        for words in sentence:
            if words not in words_in_sent:
                words_in_sent.append(words)
        for key_word in words_in_sent:
            if key_word not in d:
                d[key_word] = {}
            for accomp_word in words_in_sent:
                if key_word != accomp_word:
                    if accomp_word not in d[key_word]:
                        d[key_word][accomp_word] = 0
                    d[key_word][accomp_word] += 1
    return d

def build_semantic_descriptors_from_files(filenames):
    ''' Return a dictionary whose values are a dictionary of the number of times a word
        appears alongside the key word across all sentences in the texts in filenames.
        Assume filenames is a valid list of text files stored as strings.'''
    
    sentences = []
    for text in filenames:
        file = open(text, encoding="utf8").read().lower().replace("\n", " ").replace(',', ' ').replace('-',' ').replace('--', ' ').replace(':',' ').replace(';',' ').split('.')
        for i in range(len(file)):
            file[i] = file[i].split('!')
            for j in range(len(file[i])):
                file[i][j] = file[i][j].split('?')
                for k in range(len(file[i][j])):
                    file[i][j][k] = file[i][j][k].split()
                    sentences.append(file[i][j][k])
    dictionary = build_semantic_descriptors(sentences)
    return dictionary

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    ''' Return the string in the list choices that is most semantically similar to
        word word when tested using the similarity function similarity_fn.
        Assume word is a string, similarity_fn is a function, choices is a list 
        of strings and semantic descriptors is a dictionary of dictionaries.'''
    
    scores = []
    if word not in semantic_descriptors:
        return -1
    for choice in choices:
        if choice not in semantic_descriptors:
            scores.append(-1)
            continue
        scores.append(similarity_fn(semantic_descriptors[word], semantic_descriptors[choice]))
    return choices[scores.index(max(scores))]
    

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    ''' Return a float of the percentage of correct answers returned for the 
        semantic similarity questions in file filename.
        
        Assume filename is a valid file name stored as a string containing lines 
        of words where the first word is the base word to be compared, the second
        word is the answer, and subsequent words are the available choices.
        Assume semantic_descriptors is a dictionary of dictionaries, and similarity_fn 
        is a valid function. '''
    
    correct = 0
    
    file = open(filename, encoding="latin1").read().split("\n")
    for i in range(len(file)):
        file[i] = file[i].split()
        if len(file[i]) == 0:
            del file[i]
            i -= 1
            continue
        if file[i][1] == most_similar_word(file[i][0], file[i][2:], semantic_descriptors, similarity_fn):
            correct += 1
    
    return correct/len(file) * 100



if __name__ == "__main__":
  semantic_descriptors=build_semantic_descriptors_from_files(['pg.txt'])
  print(run_similarity_test("test.txt",semantic_descriptors,cosine_similarity))

'''Semantic Similarity

Last Modified by Elorie Bernard-Lacroix and Chaewon Lim on December 2, 2022
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the consine similarity between the sparse vectors
    vec1 and vec2, stored as dictionaries.'''
    dot_prod = 0
    vec1_sum = 0
    vec2_sum = 0
    for w in vec1:
        vec1_sum += vec1[w]**2
        if w in vec1 and w in vec2:
            dot_prod += vec1[w]*vec2[w]
    for w in vec2:
        vec2_sum += vec2[w]**2
    return dot_prod/(vec1_sum**0.5 * vec2_sum**0.5)


def build_semantic_descriptors(sentences):
    #I tried to make it work in one go but if it ends up not working or having issues,
    # we can change it so it goes through the list(of lists) twice (which is still O(n))
    word_dictionary = {}

    for sentence in sentences:
        cur_sentence_words = []
        for w in sentence:
            if w in cur_sentence_words:
                continue
            for x in cur_sentence_words:
                if x == w:
                    continue
                if w not in word_dictionary:
                    word_dictionary[w] = {x: 1}
                elif x not in word_dictionary[w]:
                    word_dictionary[w][x] = 1
                else:
                    word_dictionary[w][x] += 1

            cur_sentence_words.append(w)
            for x in cur_sentence_words:
                if x == w:
                    continue
                if x not in word_dictionary:
                    word_dictionary[x] = {w: 1}
                    word_dictionary[x][w] = 1
                elif w not in word_dictionary[x]:
                    word_dictionary[x][w] = 1
                else:
                    word_dictionary[x][w] += 1
    return word_dictionary

def build_semantic_descriptors_from_files(filenames):
    '''Input: Filenames (for data)
    Output: Semantic descriptors (dictionaries)'''
    sentences = []
    for i in range(len(filenames)):
        file = open(filenames[i], "r", encoding="latin1")
        data = file.read()
        data = data.replace("!", ".")
        data = data.replace("?", ".")
        sentences.extend(data.split("."))

    for i in range(len(sentences)):
        sentences[i] = sentences[i].split()
        for wi in range(len(sentences[i])):
            sentences[i][wi] = sentences[i][wi].strip(', - -- : ;').lower()

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    top_score = 0
    res = choices[0]  # if both aren't in the sem_descriptors, it will return the first choice by default
    for e in choices:
        if e not in semantic_descriptors or word not in semantic_descriptors:
            continue
        elif similarity_fn(semantic_descriptors[e], semantic_descriptors[word]) > top_score:
            top_score = similarity_fn(semantic_descriptors[e], semantic_descriptors[word])
            res = e

    return res

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    test = open(filename, "r", encoding="latin1")
    counter = 0
    correct = 0
    for line in test.readlines():
        counter += 1
        question = line.split()
        prediction = most_similar_word(question[0], question[2:len(question)], semantic_descriptors, similarity_fn) 
        if prediction == question[1]: #if unable to guess, guesses -1 which is always wrong
            correct += 1

    return (correct/counter) * 100






if __name__ == "__main__":
    semantic_descriptors=build_semantic_descriptors_from_files(['pg.txt'])
    print(run_similarity_test("test.txt", semantic_descriptors, cosine_similarity))
import numpy as np
import math
import os
from nltk.corpus import stopwords as sw

from queryPrep import *

'''
Prepares a dictionary for vector of words from vectors files
'''
def prepWordVectors(file, stopwords, ignoreFirstLine=False):
    vecDict = {}
    
    file = file.strip('\n')
    # For Cbow and Skipgram vectors files the first line should be ignored
    if ignoreFirstLine:
        lines = file.split('\n')[1:]
    else:
        lines = file.split('\n')
    
    for line in lines:
        line = line.strip(' ')
        columns = line.split(' ')
        word = columns[0]
        
        # Ensures stop words and empty space will not be embedded
        if word not in stopwords and word != '</s>':
            vector = np.array([float(x) for x in columns[1:]])
            vecDict[word] = vector
        
    return vecDict

'''
Gets the best term from the corpus given a word from query
'''
def getBestTerm(word, vecDict, sumVecSquaredDict):
    '''
    Given a word from query, pre-calculates and stores each term's cosine similarity with the word
    in a dictionary so that it will not need to be calculated reduplicatively later
    '''
    def getCosDict(word, vecDict, sumVecSquaredDict):
        cosDict = {}
        
        for term in vecDict:
            cosDict[term] = cos(vecDict[term], vecDict[word], sumVecSquaredDict[term], sumVecSquaredDict[word])
        
        return cosDict
    
    '''
    Calculates the cosine similarity between the vectors of word from query and term from corpus
    '''
    def cos(u, w, sumUSquared, sumWSquared):
        products = u * w
        sumProduct = np.sum(products)
        
        return sumProduct / math.sqrt(sumUSquared * sumWSquared)
    
    '''
    Given a dictionary of each term's cosine similarity with a query word, pre-calculates and stores
    the sum of all terms' cosine values for calculating translational probabilities without being
    calculated reduplicatively later
    '''
    def sumCosAllTerms(word, cosDict):
        return sum([cosDict[term] for term in cosDict if term != word])
    
    '''
    Calculates the translational probabilty for a term to a query word
    '''
    def translationalProbability(termCos, sumCos):
        return termCos / sumCos

    # Deals with the case that the word does not appear in the vector dict
    if word not in vecDict:
        return None
    
    else:
        bestTerm = ''
        highestTransProba = -(np.inf)
        # Prepares some stationary values
        cosDict = getCosDict(word, vecDict, sumVecSquaredDict)
        sumCos = sumCosAllTerms(word, cosDict)
        
        for term in vecDict:
            if term != word:
                transProba = translationalProbability(cosDict[term], sumCos)
                # Updates the term with the highest translational probability
                if transProba > highestTransProba:
                    highestTransProba = transProba
                    bestTerm = term
        
        return bestTerm

'''
Embeds new term from corpus to a query
'''
def expandQuery(query, stopwords, vecDict):
    '''
    Removes some special characters and numbers
    '''
    def removeNoise(text):
        noise = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                 '+', '=', '{', '}', '[', ']', ':', ';', '"', '<', '>', '?',
                 ',', '. ', '/', "'s", "'", '1', '2', '3', '4', '5', '6', '7',
                 '8', '9']

        for c in noise:
            text = text.replace(c, '')

        return text.replace('\n', ' ')
    
    '''
    Gets a dictionary with the sum of all vectors squared so that the sum will not
    need to be calculated again
    '''
    def getSumVecSquaredDict(vecDict):
        sumVecSquaredDict = {}
        
        for key in vecDict:
            sumVecSquaredDict[key] = sumVecSquared(vecDict[key])
        
        return sumVecSquaredDict
    
    '''
    Calculates the sum of a vector squared
    '''
    def sumVecSquared(vector):
        return np.sum(vector ** 2)
        
    '''
    Inserts the embedded new term to the query
    '''
    def insertNewTerm(pairedTerm, newTerm, query):
        queryParts = query.split(pairedTerm)
        if len(queryParts) < 2:
            return query + newTerm
        else:
            prefix = queryParts[0]
            suffix = queryParts[1]
            return prefix + pairedTerm + ' ' + newTerm + suffix

    expandedTerms = []
    pairedTerms = []
    
    # Tokenize the query without changing the origin words
    queryTokens = removeNoise(query).split(' ')
    sumVecSquaredDict = getSumVecSquaredDict(vecDict)
    
    for word in queryTokens:
        if word not in stopwords:
            bestExpandedTerm = getBestTerm(word.lower(), vecDict, sumVecSquaredDict)
            
            if bestExpandedTerm is not None:
                expandedTerms.append(bestExpandedTerm)
                pairedTerms.append(word)

    for i in range(len(expandedTerms)):
        query = insertNewTerm(pairedTerms[i], expandedTerms[i], query)
        
    return query

'''
Writes the expanded queries into a file
'''
def writeExpandedQueryFile(queryMap, stopwords, vecDict, targetPath):
    expandedQueryMap = queryMap.copy()
    for key in expandedQueryMap:
        print(key)
        expandedQueryMap[key] = expandQuery(expandedQueryMap[key], stopwords, vecDict)
    
    writeFormalQueryFile(expandedQueryMap, targetPath)
    
    
if __name__ == '__main__':
    stopwords = set(sw.words('english'))
    
    vectorsCbowS100 = prepWordVectors(open('vectors_ap8889_cbow_s100_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    vectorsCbowS300 = prepWordVectors(open('vectors_ap8889_cbow_s300_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    vectorsCbowS700 = prepWordVectors(open('vectors_ap8889_cbow_s700_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    
    vectorsSkipgramS100 = prepWordVectors(open('vectors_ap8889_skipgram_s100_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    vectorsSkipgramS300 = prepWordVectors(open('vectors_ap8889_skipgram_s300_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    vectorsSkipgramS700 = prepWordVectors(open('vectors_ap8889_skipgram_s700_w10_neg20_hs0_sam1e-4_iter5.txt', 'r').read(), stopwords, True)
    
    vectorsGloveS100 = prepWordVectors(open('vectors_ap8889_glove_s100.txt', 'r').read(), stopwords)
    vectorsGloveS300 = prepWordVectors(open('vectors_ap8889_glove_s300.txt', 'r').read(), stopwords)
    vectorsGloveS700 = prepWordVectors(open('vectors_ap8889_glove_s700.txt', 'r').read(), stopwords)
    
    queryMap = getQueryMap()
    
    outputDir = 'expanded_topics'
    
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        
    writeExpandedQueryFile(queryMap, stopwords, vectorsCbowS100, outputDir + '/expanded_topics_cbow_s100.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsCbowS300, outputDir + '/expanded_topics_cbow_s300.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsCbowS700, outputDir + '/expanded_topics_cbow_s700.trec')
    
    writeExpandedQueryFile(queryMap, stopwords, vectorsSkipgramS100, outputDir + '/expanded_topics_skipgram_s100.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsSkipgramS300, outputDir + '/expanded_topics_skipgram_s300.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsSkipgramS700, outputDir + '/expanded_topics_skipgram_s700.trec')
    
    writeExpandedQueryFile(queryMap, stopwords, vectorsGloveS100, outputDir + '/expanded_topics_glove_s100.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsGloveS300, outputDir + '/expanded_topics_glove_s300.trec')
    writeExpandedQueryFile(queryMap, stopwords, vectorsGloveS700, outputDir + '/expanded_topics_glove_s700.trec')

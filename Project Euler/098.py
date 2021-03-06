# coding=utf-8
#https://projecteuler.net/problem=98

from tools import getWordData
from gmpy2 import isqrt
from itertools import combinations

'''
Given a list of some type (e.g.: String, Integer, etc.) and a function that maps an instance of that
type into a tuple of its composites (e.g.: characters and digits, respectively), returns a hash in
which keys are composite tuples and values are lists of instances that are formed by the given
tuple. Any key-value pairs for which the length of its value list is less than 2 is removed prior to
returning the hash, effectively returning only pairs/triplets/etc. of anagrams.
'''
def getAnagrams(list, keyFunc):
    anagrams = {}
    for element in list:
        check = keyFunc(element)
        if check not in anagrams:
            anagrams[check] = [element]
        else:
            anagrams[check].append(element)
    toRemove = []
    for key in anagrams:
        if len(anagrams[key]) < 2:
            toRemove.append(key)
    for remove in toRemove:
        anagrams.pop(remove)
    return anagrams

#Returns the letters that form <word> as a sorted tuple
def getWordKey(word):
    return tuple(sorted(word))

#Returns the digits that form n as a sorted tuple
def getNumberKey(n):
    return tuple(sorted(str(n)))

#Returns the number of each individual symbol in x as a sorted tuple
def getSymbolKey(x):
    dic = {}
    for y in x:
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 1
    return tuple(sorted(dic.values()))

'''
Given an anagram pair and its corresponding potential numeric anagram pair, checks whether there
is a one-to-one mapping between characters in the anagrams and the digits in the numeric anagrams,
returning the max value if there is a match and 0 otherwise
Observation:
If there is a match, which word gets matched with which number does not matter for generating the
mapping
'''
def checkMatch(wordPair, numberPair):
    mapping = {}
    for i in xrange(len(wordPair[0])):
        mapping[wordPair[0][i]] = str(numberPair[0])[i]
    for i in xrange(len(wordPair[0])):
        if str(numberPair[1])[i] != mapping[wordPair[1][i]]:
            return 0
    return max(numberPair)

'''
Given a group of anagrams and groups of numeric anagrams, checks to see if any pair of anagrams
matches a pair of numeric anagrams (a group can consist of more than two elements; e.g.: 321 ≡ 123
≡ 213), returning the max value of all matches (the max value from previous checks is passed in for
an optimization - only groups of numeric anagrams that could yield a higher value are checked)
'''
def checkAnagrams(wordAnagrams, numberAnagrams, maxValue):
    for wordPair in combinations(wordAnagrams, 2):
        for numbers in numberAnagrams:
            if max(numbers) > maxValue:
                for numberPair in combinations(numbers, 2):
                    value = checkMatch(wordPair, numberPair)
                    if value > maxValue:
                        maxValue = value
    return maxValue

'''
Given a list of words, find the maximum value of a pair of anagrams such that substituting the same
characters with the same digits in both words both yield perfect squares
Method:
Groups words/squares on their character/digit composition. Every group of numeric anagrams is
further grouped based on the counts of their digits (e.g.: 113 and 131 would be in the same group as
722 and 272 since the digit counts in both cases is (2, 1)). Then, every group of anagrams is
checked for actual matching against groups of numerical anagrams with the same digit counts as the
character count of the anagram group.
'''
def findLargestSqAnagram():
    words = getWordData()
    wordAnagrams = getAnagrams(words, getWordKey)
    maxLength = 0
    minLength = len(wordAnagrams.keys()[0])
    for key in wordAnagrams:
        if len(key) > maxLength:
            maxLength = len(key)
        if len(key) < minLength:
            minLength = len(key)
    squares = []
    i = isqrt(10**minLength)
    while i**2 < 10**maxLength:
        squares.append(i**2)
        i += 1
    sqAnagrams = getAnagrams(squares, getNumberKey)

    symbolAnagrams = {}
    for key in sqAnagrams:
        check = getSymbolKey(key)
        if check in symbolAnagrams:
            symbolAnagrams[check].append(sqAnagrams[key])
        else:
            symbolAnagrams[check] = [sqAnagrams[key]]

    maxValue = 0
    for key in wordAnagrams:
        check = getSymbolKey(key)
        if check in symbolAnagrams:
            maxValue = checkAnagrams(wordAnagrams[key], symbolAnagrams[check], maxValue)
    return maxValue

print findLargestSqAnagram()
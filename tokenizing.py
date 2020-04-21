#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pyarabic.araby as araby
import re
from datetime import date
import cv2
import os
import requests

# 8948 tweets
tweets = json.load(open("tweets.json", 'r'))
dataset = dict()

# This regex matches everything but the Arabic letters and shadda.
all_but_arabic_letters = re.compile(u"[^\u0621-\u063A\u0641-\u064A\u0651]", flags=re.UNICODE)

# This regex matches any token that contains no Arabic letters.
# Used to discard Latin and punctuation tokens.
all_but_arabic_letters_in_token = re.compile(u"^[^\u0621-\u063A\u0641-\u064A\u0651]+$", flags=re.UNICODE)


def removeUrl(tweetText):
    return re.sub(r"http\S+", '', tweetText, flags=re.MULTILINE)


def cleanWords(words):
    a_words = []
    for word in words:
        if re.match(all_but_arabic_letters_in_token, word):  # No letters here,
            continue  # get next token.
        clean_word = re.sub(all_but_arabic_letters, "", word)
        a_words.append(clean_word)
    return a_words


# returns count of characters and unique characters
def countChars(tweetText):
    tweetText = araby.strip_tashkeel(tweetText)
    words = araby.tokenize(tweetText)  # tokenize text into words
    cleaned_words = cleanWords(words)

    add_chars = []
    for word in cleaned_words:
        for char in word:
            add_chars.append(char)
    unique_char = []
    for char in sorted(set(add_chars)):
        times = add_chars.count(char)
        unique_char.append((char, times))
    return len(tweetText), len(unique_char)


# returns count of words and unique words
def countWords(tweetText):
    tweetText = araby.strip_tashkeel(tweetText)
    words = araby.tokenize(tweetText)  # tokenize text into words
    cleaned_words = cleanWords(words)
    unique_words = []
    for word in sorted(set(cleaned_words)):
        times = cleaned_words.count(word)
        unique_words.append(word)

    return cleaned_words, unique_words
x = 0
#looping through all tweets
for tweet in tweets:
    x+=1
    key = int(tweet["tweetid"])
    value = []
    count_words, count_unique_words = countWords(tweet["text"])
    value.append(count_words)  # count of words
    value.append(count_unique_words)  # count of unique words
    row = {key: value}
    dataset.update(row)
    print ("[Tweet #"+str(x)+"] Processed")

#storing the dataset in output.json file
json.dump(dataset, open("tokens.json","w"))



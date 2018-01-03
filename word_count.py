#! python3
# -*- coding: UTF-8 -*-
# @date: 2018/1/3 14:21 
# @name: word_count
# @author：pinglin

import sys,re,collections,nltk
import codecs
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from extract_six import convert_pdf_to_txt


# patterns that used to find or/and replace particular chars or words
# to find chars that are not a letter, a blank or a quotation
pat_letter = re.compile(r'[^a-zA-Z \']+')
# to find the 's following the pronouns. re.I is refers to ignore case
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
# to find the 's following the letters
pat_s = re.compile("(?<=[a-zA-Z])\'s")
# to find the ' following the words ending by s
pat_s2 = re.compile("(?<=s)\'s?")
# to find the abbreviation of not
pat_not = re.compile("(?<=[a-zA-Z])n\'t")
# to find the abbreviation of would
pat_would = re.compile("(?<=[a-zA-Z])\'d")
# to find the abbreviation of will
pat_will = re.compile("(?<=[a-zA-Z])\'ll")
# to find the abbreviation of am
pat_am = re.compile("(?<=[I|i])\'m")
# to find the abbreviation of are
pat_are = re.compile("(?<=[a-zA-Z])\'re")
# to find the abbreviation of have
pat_ve = re.compile("(?<=[a-zA-Z])\'ve")


lmtzr = WordNetLemmatizer()


def get_words(file):
    with codecs.open(file, 'r', 'utf-8') as f:
        words_box=[]
        pat = re.compile(r'[^a-zA-Z \']+')
        for line in f:
            words_box.extend(merge(replace_abbreviations(line).split()))
    return collections.Counter(words_box)


def merge(words):
    new_words = []
    for word in words:
        if word:
            tag = nltk.pos_tag(word_tokenize(word)) # tag is like [('bigger', 'JJR')]
            pos = get_wordnet_pos(tag[0][1])
            if pos:
                lemmatized_word = lmtzr.lemmatize(word, pos)
                new_words.append(lemmatized_word)
            else:
                new_words.append(word)
    return new_words


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''


def replace_abbreviations(text):
    new_text = text
    new_text = pat_letter.sub(' ', text).strip().lower()
    new_text = pat_is.sub(r"\1 is", new_text)
    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')
    return new_text


# def append_ext(words):
#     new_words = []
#     for item in words:
#         word, count = item
#         tag = nltk.pos_tag(word_tokenize(word))[0][1] # tag is like [('bigger', 'JJR')]
#         new_words.append((word, count, tag))
#     return new_words

def write_to_file(words, file='results.txt'):
    f = open(file, 'w')
    for item in words:
        for field in item:
            f.write(str(field)+',')
        f.write('\n')

def remove_easy_words(file, counter):
    # print(counter)
    # print(counter["the"])
    with open(file, 'r') as f:
        for line in f:
            # print(counter[line.split()[0]])
            del counter[line.split()[0]]
    f.close()

if __name__=='__main__':
    print("start...")
    pdf = r'./PRACTICAL_LINUX_SECURITY_COOKBOOK.pdf'
    # pdf = r'./test.pdf'
    easy = r'./easy3000.txt'
    print("pdf2txt")
    convert_pdf_to_txt(pdf)
    book = r'./book.txt'
    print("counting...")
    words = get_words(book)
    remove_easy_words(easy, words)
    print("writing file...")
    write_to_file(words.most_common())

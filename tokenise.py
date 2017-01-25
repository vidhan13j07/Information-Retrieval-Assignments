from nltk import word_tokenize
import os
import sys
from nltk.stem import *
from nltk.tokenize import RegexpTokenizer

reload(sys)
sys.setdefaultencoding('utf8')

def tokenize(text):
    text = text.encode('ascii',errors='ignore')
    tokenizer = RegexpTokenizer(r'\w+')
    text1 = tokenizer.tokenize(text)
    x =  map(lambda x: x.lower(), text1)
    stemmer = PorterStemmer()
    stem  = [stemmer.stem(y) for y in x]
    return stem

def cal():
    path = os.path.realpath('.')
    tokenized_words = []
    for files in os.listdir(os.path.join(path, 'data')):
        with open(os.path.join(path, 'data', files), "r") as f:
            _id = files[:-4]
            data = {
                'id': _id,
                'text': tokenize(f.read())
            }
            tokenized_words.append(data)
    return tokenized_words

x = cal()

file1 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/1.txt",'r')

raw1 = file1.read()

list1 = word_tokenize(raw1)

list1 = map(lambda x: x.lower(),list1)

file1.close()

file2 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/2.txt",'r')

raw2 = file2.read()

list2 = word_tokenize(raw2)

list2 = map(lambda x: x.lower(),list2)

file2.close()

file3 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/3.txt",'r')

raw3 = file3.read()

list3 = word_tokenize(raw3)

list3 = map(lambda x: x.lower(),list3)

file3.close()

file4 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/4.txt",'r')

raw4 = file4.read()

list4 = word_tokenize(raw4)

list4 = map(lambda x: x.lower(),list4)

file4.close()

file5 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/5.txt",'r')

raw5 = file5.read()

list5 = word_tokenize(raw5)

list5 = map(lambda x: x.lower(),list5)

file5.close()

file6 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/6.txt",'r')

raw6 = file6.read()

list6 = word_tokenize(raw6)

list6 = map(lambda x: x.lower(),list6)

file6.close()

file7 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/7.txt",'r')

raw7 = file7.read()

list7 = word_tokenize(raw7)

list7 = map(lambda x: x.lower(),list7)

file7.close()

file8 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/8.txt",'r')

raw8 = file8.read()

list8 = word_tokenize(raw8)

list8 = map(lambda x: x.lower(),list8)

file8.close()

file9 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/9.txt",'r')

raw9 = file9.read()

list9 = word_tokenize(raw9)

list9 = map(lambda x: x.lower(),list9)

file9.close()

file10 = open("/home/walker/Desktop/Information-Retrieval-Assignments/data/10.txt",'r')

raw10 = file10.read()

list10 = word_tokenize(raw10)

list10 = map(lambda x: x.lower(),list10)

file10.close()

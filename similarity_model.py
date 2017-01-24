from tokenise import list1, list2,list3,list4,list5,list6,list7,list8,list9,list10
import nltk
import numpy as np
from nltk import word_tokenize
import math as m  

query_text = 'Anna hazare anti Land Acquisition Bill'

query_list = word_tokenize(query_text)

query_list = map(lambda x:x.lower(),query_list)

array_columns = query_list

freq_query = [1,1,1,1,1,1]

freq_doc1 = []

for val in array_columns:
	freq_doc1.append(list1.count(val))

freq_doc2 = []

for val in array_columns:
	freq_doc2.append(list2.count(val))

freq_doc3 = []

for val in array_columns:
	freq_doc3.append(list3.count(val))

freq_doc4 = []

for val in array_columns:
	freq_doc4.append(list4.count(val))

freq_doc5 = []

for val in array_columns:
	freq_doc5.append(list5.count(val))

freq_doc6 = []

for val in array_columns:
	freq_doc6.append(list6.count(val))

freq_doc7 = []

for val in array_columns:
	freq_doc7.append(list7.count(val))

freq_doc8 = []

for val in array_columns:
	freq_doc8.append(list8.count(val))
freq_doc9 = []

for val in array_columns:
	freq_doc9.append(list9.count(val))

freq_doc10 = []

for val in array_columns:
	freq_doc10.append(list10.count(val))

freq_array = np.array([freq_query,freq_doc1,freq_doc2,freq_doc3,freq_doc4,freq_doc5,freq_doc6,freq_doc7,freq_doc8,freq_doc9,freq_doc10])

len_array = np.zeros(10)

rows = freq_array.shape[0]

col = freq_array.shape[1]

sum = 0

for i in range(1,rows):
	for j in range(0,col):
		sum = sum + freq_array[i,j]*freq_array[i,j]
	len_array[i-1] = sum
	sum = 0

for i in range(len(len_array)):
	len_array[i] = m.sqrt(len_array[i])

def cosine_similarity(frequency_array,length_array):
	rows = frequency_array.shape[0]
	col  = frequency_array.shape[1]
	simi_array = np.zeros(10)
	sum = 0
	for i in range(1,rows):
		for j in range(0,col):
			sum = sum + frequency_array[0,j]*frequency_array[i,j]
		simi_array[i-1] = sum/(length_array[i-1]*length_array[0])
		sum = 0
	return simi_array

x = cosine_similarity(freq_array,len_array)

print x
from __future__ import division
from tokenise import list1,list2,list3,list4,list5,list6,list7,list8,list9,list10
import nltk
import numpy as np
from nltk import word_tokenize
import math as m
from itertools import imap  

query_text = 'Anna hazare anti Land Acquisition Bill'

query_list = word_tokenize(query_text)

query_list = map(lambda x:x.lower(),query_list)

array_columns = query_list

freq_query = [1,1,1,1,1,1]

freq_doc1 = []

list_array = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10]

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

sum_val = 0

for i in range(1,rows):
	for j in range(0,col):
		sum_val = sum_val + freq_array[i,j]*freq_array[i,j]
	len_array[i-1] = sum_val
	sum_val = 0

for i in range(len(len_array)):
	len_array[i] = m.sqrt(len_array[i])

def cosine_similarity(frequency_array,length_array):
	rows = frequency_array.shape[0]
	col  = frequency_array.shape[1]
	simi_array = np.zeros(10)
	sum_val = 0
	for i in range(1,rows):
		for j in range(0,col):
			sum_val = sum_val + frequency_array[0,j]*frequency_array[i,j]
		simi_array[i-1] = sum_val/(length_array[i-1]*length_array[0])
		sum_val = 0
	doc_list = [1,2,3,4,5,6,7,8,9,10]

	cos_sim = dict(zip(simi_array,doc_list))
	keylist = cos_sim.keys()
	keylist.sort()
	print "Relevance order for different document to the query (Cosine Similarity): - >>>>"
	for key in keylist:
		print "\t\t\t\t\t\t   " + str(cos_sim[key])
		print "---------------------------------------------------------------"


def eucledian_similarity(frequency_array):
	rows = frequency_array.shape[0]
	col = frequency_array.shape[1]
	simi_array = np.zeros(10)
	sum_val = 0
	for i in range(1,rows):
		for j in range(0,col):
			sum_val = sum_val + ((frequency_array[i,j] - frequency_array[0,j])**2)
		simi_array[i-1] = m.sqrt(sum_val)
		sum_val = 0
	doc_list = [1,2,3,4,5,6,7,8,9,10]
	euc_sim = dict(zip(simi_array,doc_list))
	keylist = euc_sim.keys()
	keylist.sort()
	print "Relevance order for different document to the query (Eucledian Similarity): - >>>>"
	for key in keylist:
		print "\t\t\t\t\t\t   "+ str(euc_sim[key])
		print "---------------------------------------------------------------"



def unique(a):
	return list(set(a))

def intersect(a,b):
	return list(set(a) & set(b))

def union(a,b):
	return list(set(a) | set(b))

def jaccard_coefficient(list_list,array_col):
	simi_array = np.zeros(10)
	for i in range(0,len(list_list)):
		inter = intersect(list_list[i],array_col)
		uni = union(list_list[i],array_col)
		simi_array[i] = len(inter)/len(uni)

	doc_list = [1,2,3,4,5,6,7,8,9,10]

	jac_sim = dict(zip(simi_array,doc_list))
	keylist = jac_sim.keys()
	keylist.sort()
	print "Relevance order for different document to the query (Jaccard Similarity): - >>>>"
	for key in keylist:
		print "\t\t\t\t\t\t   "+ str(jac_sim[key])
		print "---------------------------------------------------------------"


def pearson_correlation_coefficient(frequency_array):
	rows = frequency_array.shape[0]
	col = frequency_array.shape[1]
	simi_array = np.zeros(10)
	sum_val = 0
	for i in range(1,rows):
			x = frequency_array[i].tolist()
			y = frequency_array[i].tolist()
			simi_array[i-1] = pearsonr(x,y) 
	doc_list = [1,2,3,4,5,6,7,8,9,10]
	pear_sim = dict(zip(simi_array,doc_list))
	keylist = pear_sim.keys()
	keylist.sort()
	print "Relevance order for different document to the query (Pearson Correlation): - >>>>"
	for key in keylist:
		print "\t\t\t\t\t\t   "+ str(pear_sim[key])
		print "---------------------------------------------------------------"

def pearsonr(x,y):
	n = len(x)
	sum_x = float(sum(x))
	sum_y = float(sum(y))
	sum_x_sq = sum(map(lambda x : pow(x,2),x))
	sum_y_sq = sum(map(lambda x : pow(x,2),y))
	psum = sum(imap(lambda x,y : x*y , x , y))
	num = psum = (sum_x * sum_y/n)
	den = pow((sum_x_sq - pow(sum_x,2) /n) * (sum_x_sq - pow(sum_y,2) /n),0.5)
	if den == 0:
		return 0
	return num/den


cosine_similarity(freq_array,len_array)

eucledian_similarity(freq_array)

jaccard_coefficient(list_array,array_columns)

pearson_correlation_coefficient(freq_array)
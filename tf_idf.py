import math
import numpy as np


def all_words(docs):
	# Input (docs) - list of documents 
	# Output (all_words_set) - set of all the unique words in all the documents
	all_words_set = set()
	for doc in docs:
		words = doc.split(" ")
		for word in words:
			all_words_set.add(word)
	return all_words_set


def tf(all_words_set, docs):
	all_words_list  = list(all_words_set)
	tf = []
	tf.append(all_words_list)
	for doc in docs:
		doc_word_dict = {}
		doc_words = doc.split(" ")
		for word in doc_words:
			if word not in doc_word_dict:
				doc_word_dict[word] = 1
			else:
				doc_word_dict[word] += 1


		entry = []

		for word in all_words_list:
			if word in doc_word_dict:
				entry.append(doc_word_dict[word]/float(len(doc_words)))
			else:
				entry.append(0.0)

		tf.append(entry)

	return tf



def idf(all_words_set, docs):
	N = len(docs)  #No of docs
	all_words_list  = list(all_words_set)

	"""all_words_dict = {}
	for word in all_words_list:
		all_words_dict[word] = 0"""

	doc_wise_word_count = []
	for doc in docs:
		word_count_dict = {}
		words = doc.split(" ")
		for word in words:
			if word not in word_count_dict:
				word_count_dict[word] = 1
			else:
				word_count_dict[word] += 1

		doc_wise_word_count.append(word_count_dict)

	idf = []
	#idf.append(all_words_list)
	for word in all_words_list:
		count = 0
		for i in range(len(docs)): # len(doc_wise_word_count list is the same as number of docs)
			if word in doc_wise_word_count[i]:
				count +=1

		idf_value = math.log(N/count,10) 
		idf.append(idf_value)

	idf = [all_words_list] + [idf]

	return idf



def tf_idf(tf_list, idf):
	tf_idf = []
	tf_idf.append(tf_list.pop(0))
	dummy = idf.pop(0)
	idf_vector = np.array(idf[0])
	for doc in range(len(tf_list)): #length of tf_list is equal to number of docs
		a = np.array(tf_list[doc])
		value = np.multiply(a, idf_vector)
		tf_idf.append(value)

	return tf_idf








docs = ["The car is driven on the road", "The truck is driven on the highway"]
all_words_set = all_words(docs)
print("Building TF now")
tf_list = tf(all_words_set, docs)
print("\n")
#print(tf_list)
print("Building IDF now")
#print("\n")
idf = idf(all_words_set, docs)
print("\n")

print("Building TF-IDF now")
tf_idf = tf_idf(tf_list, idf)
names = tf_idf.pop(0)
print(tf_idf)
import pandas as pd
data =pd.DataFrame(dict(zip(names, tf_idf)))
print(dict(zip(names, tf_idf)))
#print(data)









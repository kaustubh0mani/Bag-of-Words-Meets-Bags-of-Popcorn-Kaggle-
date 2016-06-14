
import nltk
import pandas as pd 
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords

class BagOfWordsProcessing(object):

	@staticmethod
	def review_to_tokens(review, remove_stopwords = False):

		# Remove HTML from reviews

		review_text = BeautifulSoup(review).get_text()

		# Remove non - letters

		review_text = re.sub("[^a-zA-Z]"," ",review_text)

		# Convert words to lower case and tokenize them

		words = review_text.lower().split()

		if remove_stopwords:

			stop_words = set(stopwords.words("english"))

			words = [w for w in words if w not in stop_words]


		return words


	@staticmethod
	def 





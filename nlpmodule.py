import urllib.request
#
# response = urllib.request.urlopen('https://www.w3schools.com/python/python_casting.asp')
#
# html = response.read()

# print (html)
#-------------------
#import nltk as nlp
#nlp.download()
# paragrapha = """"
# Machine learning is a form of AI that enables a system to learn from data rather than through explicit programming.
# However, machine learning is not a simple process.
# As the algorithms ingest training data, it is then possible to produce more precise models based on that data.
# A machine-learning model is the output generated when you train your machine-learning algorithm with data. After training, when you provide a model with an input, you will be given an output. For example, a predictive algorithm will create a predictive model. Then, when you provide the predictive model with data, you will receive a prediction based on the data that trained the model.
# illustration of robot solving puzzle Iterative learning Machine learning enables models to train on data sets before being deployed. Some machine- learning models are online and continuous. This iterative process of online models leads to an improvement in the types of associations made between data elements. Due to their complexity and size, these patterns and associations could have easily been overlooked by human observation. After a model has been trained, it can be used in real time to learn from data. The improvements in accuracy are a result of the training process and automation that are part of machine learning.
# """
# sentence = tk.sent_tokenize(paragrapha)
# sentenceRough = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
# sentence = nlp.sent_tokenize(sentenceRough)
# word = nlp.word_tokenize(sentenceRough)
#
# print(sentence)
#------------------------
# import nltk
# sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
# nltk_tokens = nltk.sent_tokenize(sentence_data)
# print (nltk_tokens)
# -------------------

fileName = open("myCorp.txt", 'r')
f = fileName.read()
print(f)
print(f.split())
print(f.split('.'))

#RE
import re
tokens = re.findall("[\w']+", f)
print(tokens)

#split in Re
sentenceSplited = re.compile('[.?!]').split(f)
print(sentenceSplited)
print("-------")

#nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams, trigrams, ngrams, everygrams
# import nltk
# nltk.download('punkt')
myTokens = word_tokenize(f)
print(myTokens)

print("----")
bi= bigrams(myTokens)
tri = list(trigrams(myTokens))
print(bi)
print(tri)
ngrm = list(ngrams(myTokens, 4))
print(ngrm)
rangeGram = list(everygrams(myTokens, 2, 3))
print(rangeGram)
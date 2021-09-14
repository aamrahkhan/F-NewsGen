import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import RegexpTokenizer

filename = './data-preparation/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))



# get text from user 

user_text = input("Please enter your headline: \n")

# list_user_text = [user_text]

# print(list_user_text)

# tokenize first please


tokenizer = RegexpTokenizer(r'\w+')

tokenized_input = tokenizer.tokenize(user_text)
print(tokenized_input)

# process the text using count vect


#print(CountVectorizer().fit_transform(list_user_text))



# def cv(data):
#     count_vectorizer = CountVectorizer()
#     emb = count_vectorizer.fit_transform(data)
#     return emb, count_vectorizer

# processed_text = cv(user_text)
# processed_text_transform = processed_text.transform(processed_text)

# call predict on the processed array

# predicted_outcome = loaded_model.predict(processed_text)

# print(predicted_outcome)
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import RegexpTokenizer

filename = './data-preparation/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))



# get text from user 

user_text = input("Please enter your headline: \n")

user_text = [user_text]

# print(list_user_text)

# tokenize first please


# tokenizer = RegexpTokenizer(r'\w+')

# tokenized_input = tokenizer.tokenize(user_text)
# print(tokenized_input)
# load Pickle count vectorizer file
filename = './data-preparation/count_vectorizer.sav'
cv = pickle.load(open(filename, 'rb'))

print(loaded_model)
print(cv)

transform_input = cv.transform(user_text)
print(transform_input)

# call predict on the processed array

predicted_outcome = loaded_model.predict(transform_input)
predicted_proba = loaded_model.predict_proba(transform_input)
if predicted_outcome[0]:
    print("There is a %d chance this is FAKE NEWS. YOU LIAR." % (predicted_proba[0][1]*100))
    # print(predicted_outcome)
    # print(predicted_proba[0][1]*100)
else:
     print("There is a %d chance this is REAL NEWS. U.S.A!! FREEDOM. EAGLES...and shit" % (predicted_proba[0][0]*100))
    # print(predicted_outcome)
    # print(predicted_proba[0][0]*100)




# process the text using count vect


#print(CountVectorizer().fit_transform(list_user_text))



# def cv(data):
#     count_vectorizer = CountVectorizer()
#     emb = count_vectorizer.fit_transform(data)
#     return emb, count_vectorizer

# processed_text = cv(user_text)
# processed_text_transform = processed_text.transform(processed_text)



# predicted_outcome = loaded_model.predict(processed_text)

# print(predicted_outcome)
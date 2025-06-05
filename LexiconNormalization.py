
import nltk


from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
lem = WordNetLemmatizer()



stem = PorterStemmer()


word = "Advertising"

print("Lemmatized :",lem.lemmatize(word,"v"))

print("Stemmed :",stem.stem(word))
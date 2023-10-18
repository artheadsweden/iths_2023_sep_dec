from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

corpus = [
    'i love the book',
    'this book was not so great',
    'the fit was great',
    'i love the shoes'
]

books = 'Books'
clothing = 'Clothing'

categories = [books, books, clothing, clothing]

vectorizer = CountVectorizer(ngram_range=(1, 2))

vectors = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(vectors.toarray())

clf = SVC(kernel='linear')
clf.fit(vectors, categories)

test_corpus = [
    'i love this read',
    'such a nice hat',
    'what a great book'
]

test_categories = [books, clothing, books]

test_x = vectorizer.transform(test_corpus)

print(clf.predict(test_x))
print(clf.score(test_x, test_categories))
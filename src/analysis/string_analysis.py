from sklearn.feature_extraction.text import CountVectorizer
def bag_of_words(data, n=1):
    vectorizer = CountVectorizer(ngram_range = (1, n))
    X = vectorizer.fit_transform(data)

    return (vectorizer.get_feature_names(),X.toarray())





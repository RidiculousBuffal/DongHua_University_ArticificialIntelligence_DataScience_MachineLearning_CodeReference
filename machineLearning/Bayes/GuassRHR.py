from sklearn.feature_extraction.text import CountVectorizer
import jieba
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
path1 = "email.txt"
train_file = open(path1, 'r', encoding = "utf-8")
corpus = train_file.readlines()
split_corpus = []
for c in corpus:
    split_corpus.append(" ".join(jieba.lcut(c)))

cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
X = cv.fit_transform(split_corpus).toarray()
Y = [0] * 5000 + [1] * 5000
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size = 0.4)
gnb = GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
print (metrics.accuracy_score(y_test, y_pred))
print (metrics.confusion_matrix(y_test, y_pred))
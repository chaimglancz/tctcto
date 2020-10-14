import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, roc_auc_score


def fun_roc(X, y, classifier, label, method='decision_function'):
    classifier.fit(X, y)
    if method == 'predict_proba':
        y_scores = classifier.predict_proba(X)
        y_scores = y_scores[:, 1]
    else:
        y_scores = classifier.decision_function(X)
    fpr, tpr, _ = roc_curve(y, y_scores)
    auc = roc_auc_score(y, y_scores)
    plt.plot(fpr, tpr, label=f"{label} (auc = {auc:.3})",lw=3)


def fun_all_class(X, y):
    plt.figure(figsize=(10, 4))
    fun_roc(X, y, LogisticRegression(random_state=0), label='LogisticRegression')
    fun_roc(X, y, KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2), label='KNeighbors',
            method='predict_proba')
    fun_roc(X, y, SVC(kernel='linear', random_state=0), label='SVC linear')
    fun_roc(X, y, SVC(kernel='rbf', random_state=0), label='SVC rbf')
    fun_roc(X, y, GaussianNB(), label='GaussianNB', method='predict_proba')
    fun_roc(X, y, DecisionTreeClassifier(criterion='entropy', random_state=0), label='DecisionTree',
            method='predict_proba')
    fun_roc(X, y, RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0), label='RandomForest',
            method='predict_proba')
    fun_roc(X, y, SGDClassifier(random_state=0), label='SGD')
    plt.legend()


dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

np.random.seed(42)
y_rand = np.random.randint(0, 2, 320)

fun_all_class(X_train, y_train)
plt.show()
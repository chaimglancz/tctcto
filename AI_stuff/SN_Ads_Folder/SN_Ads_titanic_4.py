import pandas as pd
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("titanic/train.csv")
train_data.Embarked.fillna('S', inplace=True)

class AgeBucket(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X.Age // 15 * 15)


class RelativesOnboard(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X.SibSp + X.Parch)


column_transformer = ColumnTransformer([("Age_Bucket", AgeBucket(), ["Age"]), 
                                        ("Relatives_On_board", RelativesOnboard(), ["SibSp", "Parch"]), 
                                        ("one_hot_enc", OneHotEncoder(), ["Pclass","Sex","Embarked"])], 
                                        remainder='passthrough') 

preprocess_Pipeline = Pipeline([("col_trans", column_transformer), 
                                ("imputer", SimpleImputer(strategy="median"))])

X_train = preprocess_Pipeline.fit_transform(train_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']])
y_train = train_data["Survived"]

for i in [SVC(gamma="auto"), RandomForestClassifier(n_estimators=100, random_state=42)]:
    i.fit(X_train, y_train)
    y_pred = i.predict(X_train)
    print(i, '\n', confusion_matrix(y_train, y_pred))
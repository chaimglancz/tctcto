import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv('train.csv')

sub_data = data.loc[:, ['LandSlope', 'Neighborhood', 'OverallQual', 'ExterQual',
                        'GarageYrBlt', 'SaleCondition', 'TotalBsmtSF', 'GrLivArea', 'GarageArea', 'SalePrice']]

sub_data['price_group'] = pd.cut(sub_data["SalePrice"],
                                 bins=[0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, np.inf],
                                 labels=[1, 2, 3, 4, 5, 6, 7, 8])

X_train, X_test, y_train, y_test = train_test_split(sub_data.iloc[:, :-2], sub_data.iloc[:, -2],
                                                    test_size=.2,
                                                    random_state=0,
                                                    stratify=sub_data.loc[:, 'price_group'])


class Total(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame(X.TotalBsmtSF + X.GrLivArea + X.GarageArea)


Column_pipeline = ColumnTransformer([("imputer", SimpleImputer(strategy='mean'), ['GarageYrBlt']),
                              ("attribs_adder", Total(), ['TotalBsmtSF', 'GrLivArea', 'GarageArea']),
                              ('ordinal_enc_1', OrdinalEncoder(categories=[['Gtl', 'Mod', 'Sev']]), ['LandSlope']),
                              ('ordinal_enc_2', OrdinalEncoder(categories=[['Fa', 'TA', 'Gd', 'Ex']]), ['ExterQual']),
                              ("one_hot_enc", OneHotEncoder(drop='first'), ['Neighborhood', 'SaleCondition']) 
                              ], remainder='passthrough')

full_pipeline = Pipeline([('preparation', Column_pipeline), 
                          ('scaler', StandardScaler(with_mean=False)), 
                          ('regressor', RandomForestRegressor(random_state=0,max_features=6, n_estimators=193))])
full_pipeline.fit(X_train, y_train)
joblib.dump(full_pipeline, "full_pipeline.pkl")

full_pipeline_loaded = joblib.load("full_pipeline.pkl")
y_pred = full_pipeline_loaded.predict(X_test)
print(mean_squared_error(y_test, y_pred, squared=False))



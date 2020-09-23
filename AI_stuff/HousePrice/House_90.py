import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from time import time

start = time()

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


GarageYrBlt_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy='mean')),
    ('std_scaler', StandardScaler())
])

full_pipeline = ColumnTransformer([("garage", GarageYrBlt_pipeline, ['GarageYrBlt']),
                                   ("attribs_adder", Total(), ['TotalBsmtSF', 'GrLivArea', 'GarageArea']),
                                   ('ordinal_enc_1', OrdinalEncoder(categories=[['Gtl', 'Mod', 'Sev']]), ['LandSlope']),
                                   ('ordinal_enc_2', OrdinalEncoder(categories=[['Fa', 'TA', 'Gd', 'Ex']]),
                                    ['ExterQual']),
                                   ("one_hot_enc", OneHotEncoder(drop='first'), ['Neighborhood', 'SaleCondition'])
                                   ], remainder='passthrough')

X_train_prepared = full_pipeline.fit_transform(X_train)


def fun_make_reg(X, y, reg):
    """
    Please pass one of the following Regressor name as your Regression Model:

    LinearRegression()
    SVR(kernel = 'rbf')
    DecisionTreeRegressor(random_state = 0)
    RandomForestRegressor(n_estimators = 100, random_state = 42)
    'Polynomial'

    """
    if reg == 'Polynomial':
        poly_reg = PolynomialFeatures(degree=2)
        reg = LinearRegression().fit(poly_reg.fit_transform(X), y)
        return poly_reg, reg
    else:
        return reg.fit(X, y)


def fun_predict(reg, X):
    X = full_pipeline.transform(X)

    if type(reg) == tuple:
        return reg[1].predict(reg[0].fit_transform(X))
    else:
        return reg.predict(X)


def fun_check_all_reg(X_train_prepared, X_test, y_train, y_test):
    # this is a list of the regressors that we are going to use
    regressors = [LinearRegression(),
                  SVR(kernel='rbf'),
                  DecisionTreeRegressor(random_state=0),
                  RandomForestRegressor(n_estimators=100, random_state=0),
                  'Polynomial']

    # we are making a list of all the error's
    values = []
    for i in regressors:
        reg = fun_make_reg(X_train_prepared, y_train, i)
        y_pred = fun_predict(reg, X_test)
        values.append(mean_squared_error(y_test, y_pred, squared=False))

    table = pd.DataFrame(values, index=['Linear', 'SVR', 'DecisionTree', 'RandomForest', 'Polynomial'])
    return table, regressors[np.argmin(values)]


table, best_reg = fun_check_all_reg(X_train_prepared, X_test, y_train, y_test)
reg = fun_make_reg(X_train_prepared, y_train, best_reg)
y_pred = fun_predict(reg, X_test)

print(table)

end = time() - start # run time = 0:0:1
print('run time = ' + str(round(end / 3600)) + ':' + str(round((end % 3600) / 60)) + ':' + str(round(end % 60)))

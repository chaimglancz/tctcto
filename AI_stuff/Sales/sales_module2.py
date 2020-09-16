import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import time
import os
start_time = time.time()


def november_better(df):
    # we are getting the monthly sum's of all item's
    shops_month_sum = df.item_cnt_day.groupby(df.date_block_num).sum()
    shop_reg = LinearRegression().fit(shops_month_sum.index.values.reshape(-1, 1), shops_month_sum)

    # we look if there is two November's or one or None
    if 10 in shops_month_sum:
        # we are making a line from 10 tru 22 pointing to 34
        nov = 2 * shops_month_sum[22] - shops_month_sum[10]

    elif 22 in shops_month_sum:
        # we see the dif by 22 and we apply it by 34
        nov = shop_reg.predict([[34]]) + shops_month_sum[22] - shop_reg.predict([[22]])

    else:
        # we make 34 like 33
        nov = shops_month_sum[33]

    better = nov / shop_reg.predict([[34]]).item()
    return better


# we use items to see the len(items)=22170
items = pd.read_csv('items.csv')

# this is an empty df that will have all kinds (60 shops * 22170 items) 
all_kinds_df = pd.DataFrame(columns=['shop_id', 'item_id', 'item_cnt_month'])

# this is a small df that we use temporary for each shop
item_df = pd.DataFrame(np.arange(len(items)), columns=['item_id'])

# this is all the 2,935,849 previous sales
sales_train = pd.read_csv('sales_train.csv')

# we are taking the active shops that sold stuff Oct but not taking 9 and 20 because thy only sold stuff October's
active_shops = []
for i in range(60):
    one_shop_month_sum = sales_train.item_cnt_day[sales_train.shop_id == i].groupby(sales_train.date_block_num).sum()
    if 33 in one_shop_month_sum.index and i not in [9, 20]:
        active_shops.append(i)
active_sales_train = sales_train[sales_train.shop_id.isin(active_shops)]

# a loop for each shop to predict
for i in active_shops:
    # we are taking only the items that are in this shop
    current_shop_df = active_sales_train[active_sales_train.shop_id == i]
    current_items = current_shop_df.item_id.drop_duplicates().to_frame().reset_index(drop=True)

    # we are multiplying each item by 34 with a outer join
    current_items['key'] = 1
    date_block_num = pd.DataFrame({'date_block_num': np.arange(34), 'key': 1})
    items_all_months = pd.merge(current_items, date_block_num, on='key').drop("key", 1)

    # we are getting the sum's of the month's that have a sum and filling the rest with 0
    mont_sums = current_shop_df.item_cnt_day.groupby([current_shop_df.item_id,
                                                      current_shop_df.date_block_num]).sum().to_frame()
    all_mont_sm = pd.merge(items_all_months, mont_sums, on=['item_id', 'date_block_num'], how='left').fillna(0)

    # we are getting the percentage of November for this shop
    percent = november_better(current_shop_df)

    # filling 0 to clear the previous predictions here we are putting our predictions
    item_df['item_cnt_month'] = 0
    # we put here the shop id
    item_df['shop_id'] = i

    # X and y for regression
    X = np.arange(34).reshape(-1, 1)
    for j in range(0, len(all_mont_sm), 34):
        y = all_mont_sm.item_cnt_day.iloc[j:j + 34].values.reshape(-1, 1)

        # we are predicting for the 35'th month and increcing it for November
        reg = LinearRegression().fit(X, y)
        pred_34 = reg.predict([[34]]) * percent

        # we are putting here the predictions that are not below zero
        if pred_34 > 0:
            indx = all_mont_sm.loc[j, 'item_id']
            item_df.loc[indx, 'item_cnt_month'] = pred_34.item()

    # we keep on appending each shop's prediction's to all_kinds_df
    all_kinds_df = all_kinds_df.append(item_df, ignore_index=True)

# we are joining our predictions to the test
test = pd.read_csv('test.csv')
submission = pd.merge(test, all_kinds_df, on=['shop_id', 'item_id'])
submission = submission[['ID', 'item_cnt_month']]

try:
    os.mkdir('sales2_folder ')
except:
    pass
submission.to_csv('sales2_folder/submission2.csv', index=False)
print(time.time() - start_time)  # = 4:14

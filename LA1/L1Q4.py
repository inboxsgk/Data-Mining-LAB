import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

print("-"*25,"\nGowtham Karthikeyan S\n21BBS0157\nQuestion 4\n","-"*25)

data = [['Sedan', 'Red', 'Sunroof'],
        ['SUV', 'Black', 'Leather Seats'],
        ['Sedan', 'Silver', 'Sunroof'],
        ['SUV', 'Black', 'Leather Seats', 'Navigation'],
        ['Sedan', 'White', 'Sunroof'],
        ['Hatchback', 'Blue', 'Sunroof'],
        ['SUV', 'Brown', 'Leather Seats', 'Sunroof'],
        ['Sedan', 'Black', 'Navigation'],
        ['Hatchback', 'Green', 'Sunroof', 'Leather Seats'],
        ['SUV', 'White', 'Sunroof', 'Navigation'],
        ['Sedan', 'Red', 'Leather Seats'],
        ['Hatchback', 'Black', 'Sunroof', 'Navigation'],
        ['SUV', 'Silver', 'Leather Seats'],
        ['Sedan', 'Blue', 'Sunroof', 'Navigation'],
        ['Hatchback', 'White', 'Leather Seats'],
        ['SUV', 'Green', 'Sunroof'],
        ['Sedan', 'Black', 'Sunroof'],
        ['Hatchback', 'Red', 'Leather Seats', 'Navigation'],
        ['SUV', 'Blue', 'Leather Seats', 'Sunroof'],
        ['Sedan', 'White', 'Leather Seats', 'Navigation']]

te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

min_support = 0.3
frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)

print(frequent_itemsets)


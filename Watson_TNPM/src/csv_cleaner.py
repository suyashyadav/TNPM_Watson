import pandas as pd
data = pd.read_csv('testing_5725C1500_Mar.csv', sep='\t')
print (data)
data.dropna()
data.dropna().to_csv('example_clean.csv')
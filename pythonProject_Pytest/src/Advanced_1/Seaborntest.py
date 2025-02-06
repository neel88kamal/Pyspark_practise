import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

tips_df = sns.load_dataset('tips')
# tips_df.plot()
# sns.pairplot(tips_df,)
print(tips_df.head())

print(tips_df["sex"].value_counts())

sns.barplot(x="sex",y="total_bill",data=tips_df)
plt.show()
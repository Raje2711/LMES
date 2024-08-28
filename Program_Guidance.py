import pandas as pd
import plotly.express
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Surya\Desktop\Data_Science\Ras\lmes\DAY_14_CASE_STUDY_2\FlipkartSalesData.csv")
# print(df.head())
pd.set_option("display.max_columns",None)
df.dropna(how = "all", inplace = True)
print(df["brand"].unique())

print(df.columns)
# print(df.describe())
#print(df.isnull())
print(df["brand"].nunique())

a = df.loc[df["brand"] == "Alisha",'retail_price'].sum()
print("Total Retail Price-ALISHA",a)
b = df.loc[df["brand"] == "Alisha",'discounted_price'].sum()
print("Total Discounted Price-ALISHA",b)
print("_____________TOTAL NO OF BRANDS IN FLIPKART SHOPPING_____________")
counts = df["brand"].value_counts()
print(counts)
count = df["brand"].value_counts()['Slim']
print(f"Total unit sold in Slim Brand is: {count}")



filter1 = df.loc[(df["brand"]=="Alisha") & (df["product_name"]== "Alisha Solid Women's Cycling Shorts"),["brand","product_name","crawl_timestamp","product_url"]]
filter2 = df.loc[(df["product_name"]=="Alisha Solid Women's Cycling Shorts"),["retail_price","discounted_price"]]
filtered_data = pd.concat([filter1,filter2],axis =1)
final_data = pd.DataFrame(filtered_data)
print(final_data)

"""------------------TO VIEW THE PRICE DETAILS IN PLOT-----------------"""
plt.scatter(a,b,color ='blue',s=100,alpha=0.5)
plt.xlabel('Retail Price')
plt.ylabel('Discounted Price')
plt.title('Scatter Plot')
plt.grid(True)
plt.show()

import pandas as pd

#引入文件
df=pd.read_csv(r"C:\Users\fenti\OneDrive\Desktop\第一周任务\data.csv")

value_max=df.max()
value_mean=df.mean()
value_var=df.var()
value_median=df.median()

print("最大值：")
print(value_max)
print("\n平均值：")
print(value_mean)
print("\n方差：")
print(value_var)
print("\n中位数：")
print(value_median)
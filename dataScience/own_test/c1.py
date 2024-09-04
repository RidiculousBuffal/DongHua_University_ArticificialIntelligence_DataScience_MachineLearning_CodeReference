import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import tree
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('E-commerce Customer Behavior - Sheet1.csv', index_col=0)
print(df.head())
print('---')
# 统计缺失列的情况
print(df.isna().sum())
print('---')
# print(df.isnull().any())均可
# 处理缺失数据
df.fillna({
    'Age': 35,
    'Total Spend': df['Total Spend'].mean(),
    'Average Rating': df['Average Rating'].median(),
}, inplace=True)
df['Items Purchased'].fillna(method='ffill', inplace=True)
df.dropna(inplace=True)
print(df.isna().sum())
print('---')
# 统计重复值
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
# print(df.duplicated().sum())
# 统计客户数
print(pd.crosstab(df['City'], df['Membership Type']))
# 评分最高
print(df.groupby('City').aggregate({
    'Average Rating': np.mean
}).idxmax())
# 画图
fig: plt.Figure = plt.figure(figsize=(10, 10))
ax1: plt.Axes = fig.add_subplot(1, 1, 1)
df['Age'].plot(kind='hist', density=True, bins=20, ax=ax1)  # 进行标准化
df['Age'].plot(kind='kde', ax=ax1)
ax1.annotate('max point!', xytext=(20, 0.164), xy=(30, 0.163), arrowprops=dict(arrowstyle='->'), fontsize=16)
plt.savefig('fig1.png', dpi=300)
# 统计相关性
print(df[['Age', 'Total Spend', 'Items Purchased', 'Average Rating', 'Days Since Last Purchase']].corr())
ax2: plt.Axes = fig.add_subplot(1, 1, 1)
pd.plotting.scatter_matrix(df[['Age', 'Total Spend', 'Items Purchased', 'Average Rating', 'Days Since Last Purchase']],
                           diagonal='kde', color='k', ax=ax2)
plt.savefig('fig2.png', dpi=300)
# 数据处理
df.loc[df['Gender'] == 'Male', 'Gender'] = 1
df.loc[df['Gender'] == 'Female', 'Gender'] = 0
dum_city = pd.get_dummies(df['City'], prefix='City').astype(int)
df.drop(['City'], inplace=True, axis=1)
df = df.join(dum_city, how='outer')
df.loc[df['Membership Type'] == 'Gold', 'Membership Type'] = 1
df.loc[df['Membership Type'] == 'Silver', 'Membership Type'] = 0
df.loc[df['Membership Type'] == 'Bronze', 'Membership Type'] = -1
df.loc[df['Discount Applied'] == True, 'Discount Applied'] = 1
df.loc[df['Discount Applied'] == False, 'Discount Applied'] = 0
df.loc[df['Satisfaction Level'] == 'Satisfied', 'Satisfaction Level'] = 1
df.loc[df['Satisfaction Level'] == 'Neutral', 'Satisfaction Level'] = 0
df.loc[df['Satisfaction Level'] == 'Unsatisfied', 'Satisfaction Level'] = -1
print(df.head())
# 训练集划分
X = df.drop(['Satisfaction Level'], axis=1)
y = df['Satisfaction Level'].astype(int)
X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=39)
RF = RandomForestClassifier(n_estimators=40, criterion='gini', max_depth=500)
RF.fit(X_train, y_train)
print('随机森林测试集上的性能:',RF.score(x_test,y_test))
y_pred = RF.predict(x_test)
print('随机森林分类报告')
print(metrics.classification_report(y_pred,y_test))
clf = tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)
y_pred_ = clf.predict(x_test)
print('决策树测试集上的性能:',clf.score(x_test,y_test))
print('决策树分类报告')
print(metrics.classification_report(y_pred_,y_test))
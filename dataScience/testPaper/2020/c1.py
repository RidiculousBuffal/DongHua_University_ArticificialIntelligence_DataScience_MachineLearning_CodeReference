# 台风记录数据集（）记录了2014年某区域发生的台风信息，包括台风名、台风等级、气压（百帕）、移动速度（公里/时)、
# 纬度、经度、记录数、顺序、风速（米/秒）
# 等9个属性(具体说明见“数据集说明”文件)。试分析与台风等级相关的特征，并建立等级判别模型。
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import joblib
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
from sklearn.tree._export import export_text
from sklearn import metrics
from sklearn import tree
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import metrics
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 1)	从文件中读出台风数据（3分）；
df = pd.read_csv('wind.csv')
# 数据集中表示台风等级level有六个等级为：
# 热带低压、热带风暴、强热带风暴、台风、强台风、超强台风。将台风等级字符串依次替换为数字1-6（4分）；
df.replace({
    'level': {
        '热带低压': 1,
        '热带风暴': 2,
        '强热带风暴': 3,
        '台风': 4,
        '强台风': 5,
        '超强台风': 6
    }
}, inplace=True)
print(df.head())
# 计算台风的各个特征与台风等级的相关性，筛选出相关性较高（相关系数>0.6）的特征建立数据集（5分）；
features = df.columns
# print(features)
features = features.drop(['windname', 'level'])
print(features)
for i in range(0, len(features)):
    if np.abs(df['level'].corr(df[features[i]])) <= 0.6:
        df.drop(features[i], inplace=True, axis=1)

df.drop('count', axis=1, inplace=True)  # count的corr显示的是nan
print(df.head())
# 绘制图形展示筛选出的特征与台风等级的相关性
fig1: plt.Figure = plt.figure(figsize=(10, 8))
ax1: plt.Axes = fig1.add_subplot(1, 1, 1)
sns.heatmap(df[['level', 'pressure', 'windspeed']].corr(), annot=True, cmap='rainbow', fmt='.2f', ax=ax1)
ax1.set_title('corr martix')
plt.tight_layout()
plt.show()
# 按照合适比例将分析数据分为训练集和测试集（3分）；
X = df[['pressure', 'windspeed']]
y = df['level'].astype('int')
X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)
# 在训练集上建立分类模型，至少选用两种分类算法建立模型（7分）；
# 注意是分类算法,如果用聚类算法(随机森林,Kmeans是错误的)\
# 1.决策树
clf_DTree = tree.DecisionTreeClassifier()
clf_DTree = clf_DTree.fit(X_train, y_train)
# 计算分类器的score
score_DTree_train = clf_DTree.score(X_train, y_train)
print('DTree-score训练集:', score_DTree_train)
score_DTree_test = clf_DTree.score(x_test, y_test)
print('DTree-score测试集:', score_DTree_test)
# 性能评估
predicted_y_DTree = clf_DTree.predict(x_test)
print('DTree报告:\n', metrics.classification_report(y_test, predicted_y_DTree))
print('DTree-confusion matrix:')
print(metrics.confusion_matrix(y_test, predicted_y_DTree))
fName = ['pressure', 'windspeed']
clfStruc = export_text(clf_DTree, feature_names=fName)
print(clfStruc)
# SVM
clf_SVM = svm.SVC(kernel='rbf', gamma=0.7, C=1.0)
clf_SVM.fit(X_train, y_train)
y_predicted_svm = clf_SVM.predict(x_test)
# score
clf_SVM_score_train = clf_SVM.score(X_train, y_train)
print('SVM-score训练集:', clf_SVM_score_train)
clf_SVM_score_test = clf_SVM.score(x_test, y_test)
print('SVM-score测试集:', clf_SVM_score_test)
# report
print('SVM报告\n', metrics.classification_report(y_test, y_predicted_svm))
print('SVM-confusion matrix:')
print(metrics.confusion_matrix(y_test, y_predicted_svm))
# 8)	根据第7）步的运行结果，说明分类模型在台风等级判别上的性能，请描述在程序文件给出的注释行中（5分）。
# 总体来说,决策树好于SVM,SVM在测试集上性能略低,且在判断台风等级为lv2的时候精度较差

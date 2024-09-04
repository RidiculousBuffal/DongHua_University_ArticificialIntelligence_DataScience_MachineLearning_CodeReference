# 1
# 模型linreg
import pandas as pd

data = pd.read_csv('advertising.csv', index_col=0)
x = data.iloc[:, 0:3].values.astype(float)
y = data.iloc[:, 3].values.astype(float)
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(x, y)
print(linreg.intercept_, linreg.coef_)

# 模型linregTr
from sklearn import model_selection

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.35, random_state=1)
linregTr = LinearRegression()
linregTr.fit(x_train, y_train)
print(linregTr.intercept_, linregTr.coef_)

# 将模型linregTr运用到测试集
from sklearn import metrics

y_test_pred1 = linregTr.predict(x_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred1)
print('The mean squar error of test are:{:.3f}'.format(test_err1))
predict_score1 = linregTr.score(x_test, y_test)
print('The decision coeficient is:{:.3f}'.format(predict_score1))

# 将模型linreg运用到测试集
y_test_pred2 = linreg.predict(x_test)
test_err2 = metrics.mean_squared_error(y_test, y_test_pred2)
print('The mean squar error of test are:{:.3f}'.format(test_err2))
predict_score2 = linreg.score(x_test, y_test)
print('The decision coeficient is:{:.3f}'.format(predict_score2))
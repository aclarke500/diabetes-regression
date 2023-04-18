from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


diabetes = datasets.load_diabetes()
# print(diabetes.DESCR)
# print(diabetes.feature_names)

X = diabetes.data
Y = diabetes.target

# print(X.shape, Y.shape) # gives us the dimensions of our matrices

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = linear_model.LinearRegression() # I think this just gives us a shorthand
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"Coefficients: {model.coef_} \n Intercept: {model.intercept_}")
print('Mean Squared Error: %.2f' % mean_squared_error(Y_test, Y_pred))
print('Coefficient of determination : %.2f' % r2_score(Y_test, Y_pred))

# np.array(Y_test)
# sns.scatterplot(x=Y_test, y=Y_pred)

plt.title("Diabetes Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.scatter(Y_pred, Y_test)
plt.show()


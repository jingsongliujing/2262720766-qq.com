y_pred=linreg.predict(X_test)
print(y_pred)
print(type(y_pred))

print(type(y_pred),type(y_test))
print(len(y_pred),len(y_test))
print(y_pred.shape,y_test.shape)
from sklearn import metrics
import numpy as np
sum_mean=0
for i in range(len(y_pred)):
  sum_mean+=(y_pred[i]-y_test.values[i])**2
sum_erro=np.sqrt(sum_mean/50)
print("rmse by band:",sum_erro)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right")
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()







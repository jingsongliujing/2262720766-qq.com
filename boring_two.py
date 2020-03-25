#一元线性回归方程数据读取

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model

def get_data(file_name):
  data=pd.read_csv(file_name)
  X_parameter=[]
  Y_parameter=[]
  
  for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
    data['price']:
      X_parameter.append([float(single_square_feet)])
      Y_parameter.append([float(single_price_value)])
  return X_parameter,Y_paramter



#将数据拟合到线性模型
def linear_model_main(X_parameters,Y_paramters,predict_value):
  #创建线性回归对象
  regr=linear_model.LinearRegression()
  regr.fit(X_parameter,Y_parameter)
  predict_outcome=regr.predict(predict_value)
  predictions={}
  predictions['intercept']=regr.intercept_
  predictions['coefficient']=regr.coef_
  predictions['predicted_value']=predict_outcome
  return predictions



X,Y=get_data('input_data.csv')
predictvalue=700
result=linear_model_main(X,Y,predictvalue)

print(result['intercept'])
print(result['predicted_value'])







  
  
  
  
  
  
  







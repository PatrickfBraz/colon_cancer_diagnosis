"""
The codes developed in this file have the objective of meeting the necessary demands
of transformation of the target labels and validation of the models.
"""
#----------------------------------------------
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,recall_score,precision_score
#-----------------------------------------------
def transform(x):
    '''
    Function required to map target around origin
    '''
    if x == 2:
        return 1
    else:
        return -1
#-----------------------------------------------
class Metrics:
    
    def __init__(self):
        self.confusion_matrix = None
        self.Accuracy = None
        self.Precision = None
        self.Recall = None
        self.F1score = None
        self.predict = None
        
    
    def leave_one_out(self,model,train,target):
        self.predict = []
        for drop in range(0,51):
            line_droped = np.transpose(train.iloc[drop,:].values.reshape(-1,1)) 
            line_droped_target = target[drop]
            new_train = train.drop(train.index[drop], axis = 0)
            new_target = pd.DataFrame(target).drop(drop,axis = 0).values
            model.fit(new_train.values,new_target)
            predict = model.predict(line_droped)
            if predict > 0:
                self.predict.append(1)
            else:
                self.predict.append(-1)
        self.confusion_matrix = confusion_matrix(target,self.predict)
        self.evaluate_model(target,self.predict)
    
    def evaluate_model(self,y_true,y_pred):
        self.Accuracy = accuracy_score(y_true, y_pred)
        self.Precision = precision_score(y_true, y_pred)
        self.Recall = recall_score(y_true, y_pred)
        self.F1score = f1_score(y_true, y_pred)
        print('Accuracy: {} \nPrecision: {}\nRecall: {}\nF1 Score: {}'.format(self.Accuracy,
                                                                             self.Precision,
                                                                             self.Recall,
                                                                             self.F1score))
        
    def chosen_variables(self,model,train,target):
        model.fit(train,target)
        return train.columns[np.nonzero(model.coef_)[0]]


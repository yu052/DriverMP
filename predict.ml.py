import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score
import keras
from keras.models import Sequential
from keras.layers import InputLayer
from keras.layers import Dense
from keras.layers import Dropout
from keras.constraints import maxnorm
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import tensorflow as tf
import datatable as dt

# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
# load model
model = load_model('keras.nn.model.h5')
# summarize model.
model.summary()

import sys

feature_matrix=sys.argv[1]+".feature.matirx.csv"

mc3 = dt.fread(pred_file)


mc3 = mc3.to_pandas()

#mc3.drop(columns=['GENE_NAME','entrez'],inplace=True)

print(mc3.shape)

mc3.set_index('C0',inplace=True)

mc3.dropna(inplace=True)
#mc3.drop(columns=['pred'],inplace=True)
mc3=mc3*1
mc3.apply(pd.to_numeric)
mc3
mc3_pred = model.predict_classes(mc3)
mc3_pred

mc3['pred']=mc3_pred
mc3_pred_res=mc3['pred']

mc3_pred_res=pd.DataFrame(mc3_pred_res)
mc3_pred_res.pred.replace([0,1],['D','P'],inplace=True)

mc3_pred_res.to_csv(pred_file+".pred")

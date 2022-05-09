import pandas as pd
import numpy as np
import pickle
import sklearn
import json

class XGBClassifier:
    def process(self, df):
        X = df[['x7', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x18', 'x19', 'x20', 'x21', 'x22']].copy()
        X['x7'] = X['x7']/100
        X['x9'] = X['x9']/10
        
        with open('apps/ml/classifier/ohe_x2.pkl', 'rb') as f: ohe2 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x4.pkl', 'rb') as f: ohe4 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x5.pkl', 'rb') as f: ohe5 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x8.pkl', 'rb') as f: ohe8 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x15.pkl', 'rb') as f: ohe15 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x16.pkl', 'rb') as f: ohe16 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x17.pkl', 'rb') as f: ohe17 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x23.pkl', 'rb') as f: ohe23 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x24.pkl', 'rb') as f: ohe24 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x25.pkl', 'rb') as f: ohe25 = pickle.load(f)
        with open('apps/ml/classifier/ohe_x26.pkl', 'rb') as f: ohe26 = pickle.load(f)

        X2 = ohe2.transform(df['x2'].str[0].values.reshape(-1,1))
        X4 = ohe4.transform(df['x4'].str[:2].values.reshape(-1,1))
        X5 = ohe5.transform(df['x5'].values.reshape(-1,1))
        X8 = ohe8.transform(df['x8'].values.reshape(-1,1))
        X15 = ohe15.transform(df['x15'].values.reshape(-1,1))
        X16 = ohe16.transform(df['x16'].values.reshape(-1,1))
        X17 = ohe17.transform(df['x17'].values.reshape(-1,1))
        X23 = ohe23.transform(df['x23'].values.reshape(-1,1))
        X24 = ohe24.transform(df['x24'].str[:2].values.reshape(-1,1))
        X25 = ohe25.transform(df['x25'].values.reshape(-1,1))
        tmp = df['x26'].replace(to_replace='.*facebook.*', value='facebook', regex=True)
        tmp = tmp.replace(to_replace='.*play games.*', value='play games earn money', regex=True)
        X26= ohe26.transform(tmp.values.reshape(-1, 1))
     
        X = np.hstack((X.values, X2, X4, X5, X8, X15, X16, X17, X23, X24, X25, X26))
        return X

    def predict(self, input_data):
        with open('apps/ml/classifier/xgb.pkl', 'rb') as f: model = pickle.load(f)
        print(type(input_data))
        df = pd.DataFrame(input_data, index = [0])
        print(df.keys())
        X = self.process(df)
        y_pred = model.predict(X)
        y_pred_p = model.predict_proba(X)
        y_pred_p = y_pred_p.squeeze(0)
        print(y_pred_p)
        if y_pred_p[1] > 0.5:
            label = '1'
            prob = y_pred_p[1]
        else:
            label = '0'
            prob = y_pred_p[0]

        result = {'prediction': str(y_pred), 'probability': str(prob)}
        return result

import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from tqdm import tqdm

features_path = "Features/"
profile_features = "profile_features.csv"
statistical_features = "statistical_features.csv"
emotional_features = "emotional_features.csv"
textual_features = "textual_features.pkl"

users_fname = "Users.csv"
# model information
model_name = "xgb"
# model hyperparameters
params = {
    "booster": ["gbtree", "gblinear"],
    "eta": [0.3, 0.5, 0.8],
    "max_depth": [3, 6, 10, 15, 20, 60]
}
# params = {
#     "booster": ["gbtree", "gblinear"],
#     "eta": [0.3, 0.5, 0.8,1,1.5],
#     "max_depth": [3, 10, 15, 20,40, 60]
# }



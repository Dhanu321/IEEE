from utils import *
# Read users information file label them based on the number of tweets they shared
usersDF = pd.read_csv(users_fname, dtype={"user_id":str})
usersDF = label_users(1, 2,usersDF) # labelling heuristic can be changed based on application
# load features
textual_features, non_text_features = load_data()
# Read folds
foldsDF = pd.read_csv("foldsDF.csv", dtype={"user_id":str})
foldsDF = pd.merge(foldsDF, usersDF, on="user_id")
# Define results dataframe to store the scores of each fold
results = pd.DataFrame()
# begin cross validation
for fold in tqdm(range(1,11)):
    # define model
    if model_name == "xgb":
        model = XGBClassifier(verbosity=0, scale_pos_weight =4, use_label_encoder=False)
    # define train folds
    X_train = foldsDF[foldsDF["fold"] != fold]
    # oversample minority class in X_train
    X_train = oversample(X_train)
    y_train = X_train[["label"]]
    # define test fold
    X_test = foldsDF[foldsDF["fold"]==fold]
    y_test = X_test[["label"]]
    # Split features into training and testing splits
    non_text_features_tr = non_text_features.loc[X_train["user_id"].tolist()]
    non_text_features_ts = non_text_features.loc[X_test["user_id"].tolist()]

    textual_features_tr = textual_features.loc[X_train["user_id"].tolist()]["tri_grams"].to_list()
    textual_features_ts = textual_features.loc[X_test["user_id"].tolist()]["tri_grams"].to_list()
    # combine and normalize features
    X_train = preprocessing.normalize((np.concatenate((textual_features_tr, non_text_features_tr), axis=1)))
    X_test = preprocessing.normalize((np.concatenate((textual_features_ts, non_text_features_ts), axis=1)))

    # define grid search
    cv_inner = KFold(n_splits=2, shuffle=True, random_state=1)
    search = GridSearchCV(model, params, scoring='f1', cv=cv_inner, refit=True,verbose=1,return_train_score=True)
    # execute search
    model.fit(X_train, y_train["label"].tolist())
    # make predictions
    yhat = model.predict(X_test)
    # evaluate fold
    macro_f1, positive_f1 = evaluate_fold(yhat, y_test)
    # append results to results dataframe
    res = pd.DataFrame.from_records([{"fold": fold,"macro_f1": macro_f1,"positive_f1": positive_f1,}])
    results = pd.concat([results, res])
    results.to_csv("data/results_{}.csv".format(model_name), index=False)

# evaluate model by averaging the scores of all folds
results = evaluate_model(results)
# save the scores to a dataframe
results.to_csv("data/results_{}.csv".format(model_name), index=False)

# print scores
print("Done Training")
macro_f1_avg = results.loc[results['fold'] == "AVG"].iloc[0]["macro_f1"]
macro_f1_std = results.loc[results['fold'] == "STD"].iloc[0]["macro_f1"]

positive_f1_avg = results.loc[results['fold'] == "AVG"].iloc[0]["positive_f1"]
positive_f1_std = results.loc[results['fold'] == "STD"].iloc[0]["positive_f1"]

print("Average macro-f1 score = {:.3f} ({:.2f})".format(macro_f1_avg, macro_f1_std))
print("Average positive-f1 score = {:.3f} ({:.2f})".format(positive_f1_avg, positive_f1_std))

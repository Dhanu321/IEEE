from config import *

################ load_data ######################
# Function to load all feature files
# The function acquires feature file names from config file
# then csv files are read as dataframes
# non textual features are concatenated
# INPUT - No input
# OUTPUT textual features dataframe, non textual features dataframe
def load_data():
    # Read features
    X_profile = pd.read_csv("{}/{}".format(features_path,profile_features),
                            dtype={"user_id": str}).set_index("user_id").drop(columns = {"fav_growth_rate","profile_use_background_image" })
    X_statistical = pd.read_csv("{}/{}".format(features_path, statistical_features),
                                dtype={"user_id": str}).set_index("user_id")
    X_emotional = pd.read_csv("{}/{}".format(features_path, emotional_features),
                              dtype={"user_id": str}).set_index("user_id")
    X_text = pd.read_pickle("{}/{}".format(features_path, textual_features)).set_index("user_id")
    # combine features
    X_non_text = pd.concat([X_profile, X_statistical, X_emotional], axis=1)
    return X_text, X_non_text
#################################################

################ user_label #####################
# Function to label users as follows:
# if user shared N_TRUE TRUE claim (tweet or RT) and 0 FALSE claims --> Label = Not Prone to Spread Fake News [0]
# if user shared N_FALSE FALSE claim (tweet or RT) --> Label = Prone to Spread Fake News [1]
# INPUT Dataframe row, N_TRUE and N_FALSE numbers used for labeling heuristic
# OUTPUT user label [0,1]
def assign_label(row, N_TRUE, N_FALSE):
    if row["N_False"] >= N_FALSE:
        return 1
    elif row["N_False"]==0 and row["N_True"] >= N_TRUE:
        return 0
#################################################

################ label_users ######################
# Function to label users dataframe based on specific heuristic
# INPUT users Dataframe with columns N_TRUE, N_FALSE, user_id
# OUTPUT users Dataframe with column label
def label_users(N_TRUE, N_FALSE, usersDF):
    usersDF["label"] = usersDF.apply(lambda row: assign_label(row, N_TRUE, N_FALSE), axis=1)
    return usersDF
#################################################

################ oversample ######################
# Function to oversample the positive class of the training data
# INPUT X = dataframe containing user ids and their labels
# OUTPUT X = dataframe X after oversampling user ids with label 1
def oversample(X):
    X_positive = X[X["label"]==1]
    X = pd.concat([X, X_positive, X_positive])
    X = X.sample(frac=1).reset_index(drop=True)
    return X
#################################################

################ evaluate fold ##################
# Function to evaluate the predictions of the fold,
# INPUT yhat = predictions, y = ground truth
# OUTPUT macro_f1 and positive_f1 scores
def evaluate_fold(yhat, y):
    macro_f1 = f1_score(y, yhat, average='macro')
    positive_f1 = f1_score(y, yhat, pos_label=1)
    return macro_f1, positive_f1
#################################################

################ evaluate model ##################
# Function to evaluate the predictions of the model by averaging the the predictions of all folds and computes the standard deviation
# INPUT results = dataframe containing scores of all folds
# OUTPUT results dataframe after appending avg and std of the folds
def evaluate_model(results):
    # compute the average F1 and macro-F1 for all folds
    avg_macro_f1= results["macro_f1"].mean()
    avg_positive_f1 = results["positive_f1"].mean()
    # compute the standard deviation (std) of F1 and macro-F1 for all folds
    std_macro_f1= results["macro_f1"].std()
    std_positive_f1 = results["positive_f1"].std()
    # append the scores to the results dataframe
    avg_folds = pd.DataFrame.from_records([{"fold": "AVG","macro_f1": avg_macro_f1,"positive_f1": avg_positive_f1,}])
    results = pd.concat([results, avg_folds])
    std_folds = pd.DataFrame.from_records([{"fold": "STD","macro_f1": std_macro_f1,"positive_f1": std_positive_f1,}])
    results = pd.concat([results, std_folds])
    return results
#################################################




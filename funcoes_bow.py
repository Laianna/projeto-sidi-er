import optuna
from functools import partial
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.ensemble import RandomForestClassifier


def get_bag_of_words(X_train, X_valid, X_test):
    vectorizer = CountVectorizer(analyzer = "word",   
                                tokenizer = None,    
                                preprocessor = None, 
                                stop_words = None,   
                                max_features = 1500) 

    #List with BoWs
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.fit_transform(X_test)
    X_valid_vec = vectorizer.fit_transform(X_valid)

    return X_train_vec, X_valid_vec, X_test_vec


def get_best_parameters(X_train_vec, X_valid_vec, y_train, y_valid):
    study = optuna.create_study(direction="maximize")
    obj_parcial = partial(objective, X_train_vec, X_valid_vec, y_train, y_valid)
    study.optimize(obj_parcial, n_trials=20)

    return study.best_params


def objective(X_train_vec, X_valid_vec, y_train, y_valid, trial):

    param_grid = {"n_estimators": trial.suggest_int("n_estimators", 1, 1000),
                  "max_depth": trial.suggest_int("max_depth", 2, 128, log=True),
                  "criterion": trial.suggest_categorical('criterion', ["gini", "entropy"])}


    forest = RandomForestClassifier(**param_grid) 
    forest = forest.fit(X_train_vec, y_train)
    preds = forest.predict(X_valid_vec)

    return preds


def pipeline_rf(name_dataset, X_train, y_train, X_valid, y_valid, X_test, y_test):

    #Get BoW of the sentences
    X_train_vec, X_valid_vec, X_test_vec = get_bag_of_words(X_train, X_valid, X_test)
    print("vou printar X")
    print(X_train_vec)
    # #Get best parameters
    # best_params = get_best_parameters(X_train_vec, X_valid_vec, y_train, y_valid)
    
    # #Train model with best parameters
    # forest = RandomForestClassifier(**best_params) 
    # forest = forest.fit(X_train_vec, y_train)

    # #Predict test dataset 
    # label_pred = forest.predict(X_test_vec)

    #return (name_dataset, y_test, label_pred)

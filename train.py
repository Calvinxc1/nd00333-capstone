from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Workspace, Dataset


def clean_data(data):
    dummy_cols = [
        'city', 'gender', 'relevent_experience', 'enrolled_university',
        'education_level', 'major_discipline', 'experience',
        'company_size', 'last_new_job'
    ]
    x_df = pd.get_dummies(data, columns=dummy_cols).drop(columns=['enrollee_id', 'company_type'])
    y_df = x_df.pop('target').astype(float)
    return x_df, y_df


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args(args=[])

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(
        C=args.C,
        max_iter=args.max_iter,
    ).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))


# +
data_url = 'https://github.com/Calvinxc1/nd00333-capstone/raw/master/data/aug_train.csv'
dataset = pd.read_csv(data_url)
x, y = clean_data(dataset)

(x_train, x_test, y_train, y_test) = train_test_split(x, y, test_size= 0.3, random_state = 0)
# -

run = Run.get_context()


if __name__ == '__main__':
    main()



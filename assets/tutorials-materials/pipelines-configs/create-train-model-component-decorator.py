
from mldesigner import command_component, Input, Output
import mlflow
import pandas as pd
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

@command_component(
    name="train_model_decorator",
    display_name="Train a Logistic Regression Model with Decorator",
    version="3",
    environment="azureml:dmdp100env@latest"
)
def train_model_func(
    training_data: Input(type="uri_folder"),
    model_output: Output(type="mlflow_model"),
    reg_rate: float = 0.01
):
    mlflow.autolog()

    # Load data
    all_files = glob.glob(training_data + "/*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)

    X = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure',
            'TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values
    y = df['Diabetic'].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=0
    )

    model = LogisticRegression(C=1/reg_rate, solver="liblinear").fit(X_train, y_train)

    # Save to output directory
    mlflow.sklearn.save_model(model, model_output)

    # Evaluate
    y_scores = model.predict_proba(X_test)
    auc = roc_auc_score(y_test, y_scores[:,1])
    print("AUC:", auc)

    fpr, tpr, _ = roc_curve(y_test, y_scores[:,1])
    plt.plot([0, 1], [0, 1], "k--")
    plt.plot(fpr, tpr)
    plt.savefig("ROC-Curve.png")

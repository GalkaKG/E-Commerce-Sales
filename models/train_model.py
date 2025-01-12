import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

def train_and_save_model(data):
    cols = ['fulfilment', 'ship_service_level', 'qty', 'amount', 'ship_postal_code', 'b2b', 'month']
    Y = data['Courier Status']
    X = data[cols]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=45)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"RF Model Accuracy: {accuracy:.2f}")
    print('_'*30)

    report = classification_report(y_test, predictions)
    print(report)

    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

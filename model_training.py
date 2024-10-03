from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

def train_model(df):
    """Train RandomForest model and evaluate its performance."""
    X = df[['Transferror_ID', 'Transferror_Name', 'Transferror_Bank', 'Category']]  # Features
    y = df['Transferror_Type']  # Labels

    # Handle missing values
    X = X.replace("Unknown", np.nan).ffill()
    
    # Convert categorical variables to numeric
    X = pd.get_dummies(X)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Classification Report:\n {classification_report(y_test, y_pred, zero_division=0)}")
    
    return model

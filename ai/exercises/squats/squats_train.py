import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv('squats_data.csv')

# ... [rest of your training code] ...
X = df.drop('label', axis=1)
y = df['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier with parameters to prevent overfitting
clf = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=4, min_samples_leaf=4, random_state=42)

# Perform grid search to find the best parameters to prevent overfitting
param_grid = {
    'max_depth': [5, 10, 15, None],  # None means no limit
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2, 4],
    'n_estimators': [50, 100, 200]
}
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Use the best estimator found by the grid search
best_clf = grid_search.best_estimator_

# Make predictions on the test set using the best estimator
y_pred = best_clf.predict(X_test)

# Print the accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Best parameters: {grid_search.best_params_}")

# Save the trained model using pickle
with open('trained_squats_model.pkl', 'wb') as file:
    pickle.dump(best_clf, file)

import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# 1. Create dummy data (Replace this with your actual X_train, y_train)
X_train = np.array([[1, 20], [2, 30], [3, 40], [4, 50]])
y_train = np.array([0, 0, 1, 1])

# 2. Initialize and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 3. Save the trained model to a file
file_path = "income_model.pkl"

try:
    with open(file_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model successfully saved to {file_path}")
except Exception as e:
    print(f"An error occurred while saving: {e}")

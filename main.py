import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data.csv")

features = data.drop("income", axis=1)
target = data["income"]

features = pd.get_dummies(features)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Example input prediction (modify columns as per dataset)
# sample = [[35, 13, 40]]
# sample_df = pd.DataFrame(sample, columns=features.columns[:3])
# sample_pred = model.predict(sample_df)
# print("Prediction for sample input:", sample_pred[0])

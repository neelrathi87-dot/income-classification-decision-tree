# 🟢 Income Classification using Decision Tree

---

## 📄 Project Overview
Objective: To build a machine learning model that predicts whether an individual's annual income exceeds $50,000 based on demographic and employment data.

---

## 🎯 Objectives
-Develop a predictive model to classify individual income levels.
-Train a Decision Tree algorithm on demographic and employment datasets.
-Export the trained model into a pickle file for seamless integration.
-Ensure high classification precision to accurately identify high-income earners.

---

## 🧠 Approach
1. **Data Collection:** Utilize a census dataset containing demographic features like age, education, occupation, and capital gain.
2. **Data Preprocessing:** Handle missing values, encode categorical variables into numerical values, and scale features for consistency.
3. **Model Building:** Implement a Decision Tree Classifier to establish a logical hierarchy for predicting income brackets.
4. **Training:** Train the model on the processed dataset and save the state as a serializable file (.pkl file).
5. **Prediction:** Load the saved model to classify income levels for new individual data points without needing to retrain.

---

## 🗃 Dataset
Source: Kaggle

Download from Google Drive:
https://drive.google.com/file/d/1XshrDxSDebccOplyVthf-b9-0BFajS_j/view?usp=drive_link



## 🧠 Trained Model
Pre-trained Decision Tree model (.pkl):
https://drive.google.com/file/d/1Ti5JjDRQJyp_wLy7w54AxUAILuuli8we/view?usp=drive_link



---

## 🔄 Project Flow
1. Load and preprocess the dataset: Import census data, handle missing values, and encode categorical features into numerical values.
2. Configure Decision Tree architecture: Initialize the classifier and set parameters like maximum depth to prevent overfitting.
3. Train the model and save it as income_model.pkl: Fit the model on the training data and export it using the Pickle library.
4. Run predict_income.py to classify income: Load the saved .pkl file to make predictions on new user data or test samples.

---

## 📊 Model Evaluation
- Accuracy on training dataset: ~85% - 90%, demonstrating strong learning of census patterns.
- Accuracy on validation dataset: ~82% - 85%, indicating good generalization to unseen data.
- Performance Metrics: High precision and recall for identifying the <=50K and >50K income     brackets.
- Model Flexibility: The Decision Tree can be fine-tuned or retrained with updated             demographic data as economic trends change.
  
---

  💻 Technology Used
- **Programming Language:** Python 3.x
- **Libraries:** Scikit-learn, Pandas, Pickle, NumPy
- **IDE/Platform:** VS Code, Jupyter Notebook, or PyCharm

---

## ▶ How to Run

# 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


# 2️⃣ Train the Model (Optional)

If you want to retrain the Decision Tree model yourself:

```bash
python train_model.py
```

# 3️⃣ Run Income Prediction
To test the model and predict income levels:
```bash
python predict_income.py
```

# 🚀 Future Enhancements
Implement multi-class classification for granular income brackets (e.g., Low, Middle, High).

Integrate additional financial features like credit scores or debt-to-income ratio.

Deploy the model as a REST API using Flask or FastAPI for easy web integration.

Develop an interactive dashboard using Streamlit to visualize demographic trends.

# 📝 Author

Neel Rathi

Email: neelrathi87@gmail.com

Internship Project: Naviotech Solution
# 🙏 Acknowledgments

Open-source contributions for Scikit-learn, Pandas, and NumPy libraries.

UCI Machine Learning Repository for providing the Adult Census Income dataset.



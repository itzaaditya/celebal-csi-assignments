# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
# app.py
import streamlit as st
import numpy as np
import pickle
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Iris dataset for feature names
iris = load_iris()

# App title
st.title("🌸 Iris Flower Classification")
st.write("Input flower measurements to classify Iris species")

# Sidebar inputs
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)[0]
prediction_proba = model.predict_proba(input_data)

# Output
st.subheader("📌 Prediction")
st.write(f"Predicted Species: **{iris.target_names[prediction]}**")

st.subheader("🔍 Prediction Probabilities")
st.bar_chart(prediction_proba[0])

# Bonus: Visualize input on feature distribution
st.subheader("📊 Your Input Compared to Dataset")

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
features = iris.feature_names
values = [sepal_length, sepal_width, petal_length, petal_width]

for i, ax in enumerate(axs.flat):
    ax.hist(iris.data[:, i], bins=20, alpha=0.6, label='Dataset')
    ax.axvline(values[i], color='red', linestyle='dashed', linewidth=2, label='Your Input')
    ax.set_title(features[i])
    ax.legend()

st.pyplot(fig)

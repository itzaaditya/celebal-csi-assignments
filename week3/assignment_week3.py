import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = sns.load_dataset('titanic')

print(titanic.head())

sns.set(style='darkgrid')

plt.figure(figsize=(6,4))
sns.countplot(data=titanic, x='survived')
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=titanic, x='sex', hue='survived')
plt.title("Survival by Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=titanic, x='pclass', hue='survived')
plt.title("Survival by Passenger Class")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(titanic['age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
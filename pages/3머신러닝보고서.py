import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st

# 데이터 불러오기

df = pd.read_csv('Obesity Classification.csv')


st.sidebar.header('📊 머신러닝 보고서')

st.header(' 머신러닝 보고서 분석',divider='rainbow')
st.write(df)

st.markdown('''
    이 웹앱은 Obesity Classification.csv 비만 분류 데이터를 분석합니다. 데이터셋은 BMI (체질량지수) 기반의 비만 여부를 분류합니다.
    이 데이터셋은 연령, 성별, BMI 등 여러 특성을 사용하여 비만 여부를 예측합니다.
   
            ''')

le= LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df.drop(labels='ID',axis=1,inplace=True)

# 모델 학습
X = df.drop('Label', axis=1)
y = df['Label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
RFclassifier = RandomForestClassifier()

# Train the classifier on the training data
RFclassifier.fit(X_train, y_train)


# Prédictions sur l'ensemble de test
y_pred = RFclassifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Évaluation du modèle
accuracy = accuracy_score(y_test, y_pred)
st.write(f'Accuracy: {accuracy:.2f}')

# Rapport de classification
st.write(classification_report(y_test, y_pred))

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
fig=plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu", fmt='d', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
st.pyplot(fig)




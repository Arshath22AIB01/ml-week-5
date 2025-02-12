import streamlit as st
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Streamlit app title
st.title("Tennis Match Prediction")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data from CSV
    data = pd.read_csv(uploaded_file)
    st.write("The first 5 values of the data are:")
    st.write(data.head())

    # Obtain Train data and Train output
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]

    st.write("The first 5 values of train data are:")
    st.write(X.head())

    st.write("The first 5 values of train output are:")
    st.write(y.head())

    # Convert categorical features into numerical values
    le_outlook = LabelEncoder()
    X['Outlook'] = le_outlook.fit_transform(X['Outlook'])

    le_Temperature = LabelEncoder()
    X['Temperature'] = le_Temperature.fit_transform(X['Temperature'])

    le_Humidity = LabelEncoder()
    X['Humidity'] = le_Humidity.fit_transform(X['Humidity'])

    le_Windy = LabelEncoder()
    X['Windy'] = le_Windy.fit_transform(X['Windy'])

    st.write("Now the train data is:")
    st.write(X.head())

    le_PlayTennis = LabelEncoder()
    y = le_PlayTennis.fit_transform(y)
    st.write("Now the train output is:")
    st.write(y)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    # Train the Naive Bayes classifier
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Calculate accuracy
    accuracy = accuracy_score(classifier.predict(X_test), y_test)
    st.write("Accuracy is:", accuracy)

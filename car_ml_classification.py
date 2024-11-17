import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

st.set_page_config(layout='wide', page_title='Classificação de Veículos')


@st.cache_data
def load_data_and_model():
    """
    Loads vehicle classification data, encodes categorical features, splits the data into training and testing sets,
    trains a Categorical Naive Bayes model, and returns the encoder, trained model, and accuracy score.

    Returns:
        encoder (OrdinalEncoder): The encoder used for transforming categorical features.
        model (CategoricalNB): The trained Naive Bayes model.
        accuracy (float): The accuracy score of the model on the test data.
    """

    # The function reads a CSV file named
    # 'car_ml_classification.csv' into a DataFrame.
    cars = pd.read_csv('car_ml_classification.csv', sep=',')
    # An OrdinalEncoder is instantiated.
    encoder = OrdinalEncoder()

    # Each column in the DataFrame, except for 'class',
    # is converted to a categorical type.
    for col in cars.columns.drop('class'):
        cars[col] = cars[col].astype('category')

    # The target labels are extracted and encoded as categorical codes

    X_encoded = encoder.fit_transform(cars.drop('class', axis=1))
    # A NumPy array of encoded features

    y = cars['class'].astype('category').cat.codes
    # A Pandas Series of encoded target labels.

    # plit data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)
    # Train a CategoricalNB model and predict test data.
    model = CategoricalNB()
    model.fit(X_train, y_train)

    # Calculate and return the accuracy score.
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return encoder, model, accuracy, cars


encoder, model, accuracy, cars = load_data_and_model()

st.title('Previsão de qualidade de veículo')
st.write(f'Acuracia do modelo: {accuracy:.2f}')

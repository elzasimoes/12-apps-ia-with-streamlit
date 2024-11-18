"""
Benchmarking of temporal series -
Analysis of temporal series:
Compare time series for benchmarking,
Using analytical methods to evaluate and improve predictions.
"""

import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from pmdarima import auto_arima
from statsmodels.tsa.api import ExponentialSmoothing, Holt

st.set_page_config(page_title='Benchmark de Séries Temporais', layout='wide')
st.title('Benchmark de Séries Temporais')


def load_data(uploaded_file):
    """
    Load data from an uploaded file.

    Parameters
    ----------
    uploaded_file : UploadedFile
        The file uploaded by the user.

    Returns
    -------
    DataFrame
        A pandas DataFrame containing the data from the uploaded file.
    """
    data = pd.read_csv(uploaded_file, header=None)
    return data


def plot_forecasts(actual, forecasts, titles):
    """
    Plots the actual data and forecasted time series on a single graph.

    Parameters:
    actual (array-like): The actual observed data points.
    forecasts (list of array-like): A list of forecasted data series.
    titles (list of str): Titles corresponding to each forecast series for labeling.

    Returns:
    matplotlib.pyplot: The plot object with the actual and forecasted data series.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Dados Atuais')
    for forecast, title in zip(forecasts, titles):
        plt.plot(np.arange(len(actual), len(actual) + len(forecast)), forecast, label=title)
    plt.legend()
    plt.title('Benchmark de Séries Temporais')
    plt.grid(True)
    return plt


def forecast_methods(train, h, methods):
    """
    Generate forecasts using specified methods for a given training dataset.

    Parameters:
    train (pd.Series): The training data series used for forecasting.
    h (int): The forecast horizon, indicating the number of periods to predict.
    methods (dict): A dictionary specifying which forecasting methods to use,
        with keys as method names ('naive', 'mean', 'drift', 'holt', 'hw', 'arima')
        and values as booleans indicating whether to apply the method.

    Returns:
    tuple: A tuple containing two lists:
        - forecast (list): A list of forecasted values for each selected method.
        - titles (list): A list of method names corresponding to each forecast.
    """
    forecast = []
    titles = []

    if methods['naive']:
        naive_forecast = np.tile(train.iloc[-1], h)
        forecast.append(naive_forecast)
        titles.append('Naive')

    if methods['mean']:
        mean_forecast = np.tile(train.mean(), h)
        forecast.append(mean_forecast)
        titles.append('Mean')

    if methods['drift']:
        drift_forecast = train.iloc[-1] + (np.arange(1, h + 1) * ((train.iloc[-1] - train.iloc[0]) / (len(train) - 1)))
        forecast.append(drift_forecast)
        titles.append('Drift')

    if methods['holt']:
        holt_forecast = Holt(train).fit().forecast(h)
        forecast.append(holt_forecast)
        titles.append('Holt')

    if methods['hw']:
        hw_forecast = ExponentialSmoothing(train, seasonal='additive', seasonal_periods=12).fit().forecast(h)
        forecast.append(hw_forecast)
        titles.append('HW Additive')

    if methods['arima']:
        arima_model = auto_arima(train, seasonal=True, m=12, suppress_warnings=True)
        arima_forecast = arima_model.predict(n_periods=h)
        forecast.append(arima_forecast)
        titles.append('ARIMA')

    return forecast, titles


with st.sidebar:
    uploaded_file = st.file_uploader('Escolha um Arquivo CSV', type='csv')

    if uploaded_file is not None:
        data_range = st.date_input('Informe o Período', [])
        forecast_horizon = st.number_input('Informe o Perído de Previsão', min_value=1, value=24, step=1)
        st.write('Escolha os Métodos de Previsão:')

        methods = {
            'naive': st.checkbox('Naive', value=True),
            'mean': st.checkbox('Mean', value=True),
            'drift': st.checkbox('Drift', value=True),
            'holt': st.checkbox('Holt', value=True),
            'hw': st.checkbox('Holt-Winters', value=True),
            'arima': st.checkbox('ARIMA', value=True),
        }
        process_button = st.button('Processar')

if uploaded_file is not None:
    data = load_data(uploaded_file)

    if process_button and len(data_range) == 2:
        col1, col2 = st.columns([1, 4])

        with col1:
            st.dataframe(data)
        with col2:
            with st.spinner('Processando... Por Favor Aguarde!'):
                start_date, end_date = data_range
                train = data.iloc[:, 0]
                forecasts, titles = forecast_methods(train, forecast_horizon, methods)
                plt = plot_forecasts(train, forecasts, titles)
                st.pyplot(plt)

    elif process_button:
        st.warning('Por favor selecioone um perído de datas válidos')
else:
    st.sidebar.warning('Faça upload de um arquivo csv')

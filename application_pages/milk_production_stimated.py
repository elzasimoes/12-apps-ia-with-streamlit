"""Time Series: Use time series models to predict milk production,
analyzing temporal patterns and seasonality.

This code snippet is a Streamlit application for analyzing
and forecasting milk production using time series models.
It allows users to upload a CSV file containing milk production data,
set initial parameters,
and process the data to generate forecasts and visualizations.
https://www.notion.so/elzasimoes/IA-Streamlit-Estimativa-da-Produ-o-de-Leite-S-ries-Temporais-1411bb8db8cb802397e4d333ca9171a9?pvs=4

"""

from datetime import date
from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

st.set_page_config('Análise e Previsão de Séries Temporais', layout='wide')

st.markdown('### Sistema de Análise e Previsão de Séries Temporais')

with st.sidebar:
    # The user uploads a CSV file containing milk production data.
    uploaded_file = st.file_uploader(label='Carregue o arquivo da previsão', type='csv')

    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))

        milk_data = pd.read_csv(stringio, header=None)

        # The user sets the initial date and the number of months to forecast.
        initial_date = date(2000, 1, 1)
        inital_period = st.date_input('Período Inicial da Série', initial_date)
        prev_period = st.number_input('Informe quantos meses você quer prever', min_value=1, max_value=48, value=12)
        processing = st.button('Processar')

if uploaded_file is not None and processing is True:
    try:
        ts_data = pd.Series(
            milk_data.iloc[:, 0].values,
            index=pd.date_range(start=inital_period, periods=len(milk_data), freq='M'),
        )
        # The application processes the data, decomposes the time series, and fits a SARIMAX model.
        decompose = seasonal_decompose(ts_data, model='additive')
        fig_decompose = decompose.plot()
        fig_decompose.set_size_inches(10, 8)

        # Forecasts are generated and visualized alongside the original data.
        model = SARIMAX(ts_data, order=(2, 0, 0), seasonal_order=(0, 1, 1, 12))
        model_fit = model.fit()
        prev = model_fit.forecast(steps=prev_period)

        fig_prev, ax = plt.subplots(figsize=(10, 5))
        ax = ts_data.plot(ax=ax)
        prev.plot(ax=ax, style='r--')

        st.write('Decomposição')
        st.pyplot(fig_decompose)

        st.write('Previsão')
        st.pyplot(fig_prev)

        st.write('Dados da previsão')
        st.dataframe(prev)

    except FileNotFoundError:
        st.error('Arquivo não encontrado. Verifique o caminho.')
    except Exception as e:
        st.error(f'Ocorreu um erro ao processar os dados: {e}')

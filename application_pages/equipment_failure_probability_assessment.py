"""Equipment Failure Probability Assessment - Poisson Distribution:
Implement statistical models to predict equipment failure by applying
the Poisson distribution theory.
This code is a Streamlit application that calculates and visualizes the probability of equipment
failure using the Poisson distribution. It allows users to select the type of probability calculation and input the current number of occurrences, then displays the results using both Matplotlib and Plotly Express.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from scipy.stats import poisson

st.set_page_config(page_title='Probabilidade de falhas em equipamentos')

st.markdown('### Probabilidade de falhas em equipamentos')

options = ['Prob. Exata', 'Menos que', 'Mais que']
with st.sidebar:
    st.header('Configurações')
    # A string indicating the type of probability calculation.
    calc_type = st.radio('Selecione o Cálculo: ', options=options)
    # An integer representing the current number of occurrences, with a default value of 2.
    atual_failure = st.number_input('Ocorrência Atual', min_value=1, max_value=99, value=2)
    processing = st.button('Processar')

# The user selects a calculation type and inputs the current number of occurrences.
# Upon clicking 'Processar', the code calculates the Poisson probability based on the selected type.
# It generates a range of values around the current occurrence and computes the probability for each.

if processing is True:
    lamb = atual_failure
    inic = lamb - 2
    fim = lamb + 2
    x_vals = np.arange(inic, fim + 1)

    if calc_type == 'Prob. Exata':
        probs = poisson.pmf(x_vals, lamb)
        title = 'Probabilidade de ocorrência'

    if calc_type == 'Menos que':
        probs = poisson.cdf(x_vals, lamb)
        title = 'Probabilidade de ocorrência igual ou menor que:'

    if calc_type == 'Mais que':
        probs = poisson.sf(x_vals, lamb)
        title = 'Probabilidade de ocorrência mais que:'

    # The results are visualized using Matplotlib and Plotly Express,
    # displaying both static and interactive charts.
    z_vals = np.round(probs, 4)
    labels = [f'{i} prob.: {p}' for i, p in zip(x_vals, z_vals)]

    st.markdown('### Gráfico com Matplot Lib')
    fig, ax = plt.subplots()
    ax.bar(x_vals, probs, tick_label=labels, color=plt.cm.gray(np.linspace(0.4, 0.8, len(x_vals))))
    ax.set_title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

    probs_percentage = probs * 100

    df = pd.DataFrame({'Ocorrências': x_vals, 'Porcentagem (%)': probs_percentage})

    st.markdown('### Gráfico interativo com Plotly Express')
    fig = px.bar(
        df,
        x='Ocorrências',
        y='Porcentagem (%)',
        text='Porcentagem (%)',
        title=title,
        labels={'Porcentagem (%)': 'Porcentagem (%)', 'Ocorrências': 'Número de Ocorrências'},
        template='plotly_white',
    )

    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(xaxis_title='Número de Ocorrências', yaxis_title='Porcentagem (%)')

    st.plotly_chart(fig, use_container_width=True)

"""This code snippet creates and fits a linear regression model using the
LinearRegression class from the sklearn library.
It uses the input features X and the target variable y to train the model.
https://www.notion.so/elzasimoes/IA-Streamlit-Prevendo-Custos-para-abrir-uma-Franquia-Regress-o-1411bb8db8cb809da5a1ee80e1317b6b?pvs=4
"""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression

st.title('Previsão inicial de custo para Franquia utilizando regressão Linear')

franchise_data = pd.read_csv('./franchise_linear_regression.csv', sep=';')

X = franchise_data[['FrqAnual']]
# A DataFrame containing the feature(s) for the linear regression model.
y = franchise_data['CusInic']
# y: A Series containing the target variable for the linear regression model.

# Fit the linear regression model
model = LinearRegression().fit(X, y)

st.markdown('### Dados utilizados para treinar o modelo')
st.dataframe(franchise_data.head(), hide_index=True)

st.markdown('### Gráfico de dispersão com Matplot Lib')
fig, ax = plt.subplots()
ax.scatter(X, y, color='blue', label='Data Points')
ax.plot(X, model.predict(X), color='red', label='Model Prediction')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.legend()
# Display a matplotlib.pyplot figure
st.pyplot(fig)

st.markdown('### Gráfico de dispersão com Plotly Express')
fig_2 = px.scatter(
    franchise_data,
    x='FrqAnual',
    y='CusInic',
    labels={'FrqAnual': 'Frequência Anual', 'CusInic': 'Custo Inicial'},
    title='Relação entre Frequência Anual e Custo Inicial com Regressão Linear',
    trendline=None,
)

fig_2.add_scatter(
    x=franchise_data['FrqAnual'],
    y=model.predict(franchise_data[['FrqAnual']]),
    mode='lines',
    name='Linha de Regressão',
    line=dict(color='red', dash='dash'),
)
# Display an interactive Plotly chart.
st.plotly_chart(fig_2)


st.header('Valor anual da franquia: ')

new_value = st.number_input(
    'Insira novo valor',
    min_value=1.0,
    max_value=9999.0,
    value=1500.0,
    step=0.01,
)
processing = st.button('Processar')

if processing is True:
    new_value_data = pd.DataFrame([new_value], columns=['FrqAnual'])
    prev = model.predict(new_value_data)
    st.header(f'Nova previsão de custo inicial R$: {prev[0]:.2f}')

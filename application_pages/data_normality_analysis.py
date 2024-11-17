"""
Normal distribution: explore statistical techniques to verify the normality of the data sets,
essential in many statistical analyzes and inferences.
This code sets up a Streamlit application to test the normality of a dataset using statistical techniques.
It allows users to upload a CSV file, then generates a histogram and a QQ plot of the data.
It also performs a Shapiro-Wilk test to determine
if the data follows a normal distribution.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from scipy import stats

st.set_page_config('Teste de normalidade dos dados', layout='wide')

st.markdown('### Teste de normalidade')

with st.sidebar:
    # The user uploads a CSV file via the Streamlit sidebar.
    upload_file = st.file_uploader('Escolha o arquivo:', type='csv', accept_multiple_files=False)
    process_button = st.button('Processar')

if process_button is True and upload_file is not None:
    try:
        # The code reads the CSV file and checks for valid data.
        data = pd.read_csv(upload_file, header=None)
        if data.empty or data.iloc[:, 0].isnull().all():
            st.error('O arquivo está vazio ou a primeira coluna não tem dados válidos')
            raise (FileExistsError, FileNotFoundError)

        fig1, fig2 = st.columns(2)

        with fig1:
            # It generates a histogram and a QQ plot of the first column of the dataset.
            fig_hist, ax_hist = plt.subplots()
            ax_hist.hist(data.iloc[:, 0].dropna(), bins='auto', color='blue', alpha=0.7, rwidth=0.85)
            ax_hist.set_title('Histograma')
            st.pyplot(fig_hist)

        with fig2:
            fig_qq, ax_qq = plt.subplots()
            stats.probplot(data.iloc[:, 0].dropna(), dist='norm', plot=ax_qq)
            ax_qq.set_title('QQ Plot')
            st.pyplot(fig_qq)

        # A Shapiro-Wilk test is performed on the data.
        shapiro_test = stats.shapiro(data.iloc[:, 0].dropna())
        st.write(f'Valor de P: {shapiro_test.pvalue: .5f}')

        # The result of the test is displayed, indicating whether the data is normally distributed.
        SHAPIRO_ACCEPT_VALUE = 0.05
        if shapiro_test.pvalue > SHAPIRO_ACCEPT_VALUE:
            st.success('Não existem evidências para rejeitar a hipótese de normalidade dos dados')

        else:
            st.error('Existem evidências suficientes para rejeitar a hipótese de normalidade dos dados')

    except FileNotFoundError:
        st.error('Arquivo não encontrado')
    except Exception as e:
        st.error(e)

import streamlit as st

pages = {
    '12 Aplicações Web de Inteligência Artificial': [
        st.Page(
            'franchise_linear_regression.py',
            title='Prevendo Custos para Abrir Franquia (Regressão)',
        ),
        st.Page(
            'car_ml_classification.py',
            title='Prevendo a qualidade dos Veículos',
        ),
    ],
}

pg = st.navigation(pages)
pg.run()
